#!/usr/bin/env python3
"""
Automated Open Source Contributions Table Updater for Ankit Dhandharia's Profile README.
Fetches public pull requests across external repositories, generates dynamic status badges,
and updates the markdown table between comment tags.
"""

import os
import re
import json
import urllib.request
import subprocess
from collections import defaultdict

CURATED_IMPACTS = {
    'unit8co/darts': 'Fixed multithreaded race condition in `_model_call` during parallel Optuna sweeps (`n_jobs>1`); documented `window` parameter in `CauchyNLLScorer`.',
    'protocolbuffers/protobuf': 'Included duplicate collision key in C# `MapField.Add` exception message to accelerate debugging in downstream cloud logging services.',
    'deepspeedai/DeepSpeed': 'Fixed AutoSP test suite expecting LLM attention layers to be auto-wrapped with `DistributedAttention`, properly matching sequence parallelism architecture.',
    'onnx/onnx': 'Handled legacy Resize inputs in reference implementation and preserved exact nearest-neighbor values across opset 10/11 transitions.',
    'pytorch/vision': 'Fixed reference script `evaluate()` crashing with uninitialized default process group when run outside distributed environments.',
    'dmlc/xgboost': 'Added strict Python type annotations to config and tree regularization test suites and enabled mypy CI enforcement.',
    'meta-pytorch/botorch': 'Introduced pluggable `cat_kernel_factory` in `MixedSingleTaskGP` to support domain-specific categorical kernels alongside continuous dimensions.',
    'awslabs/gluonts': 'Prevented unintended CUDA context initialization by keeping PyTorch predictors strictly on CPU when training with `accelerator="cpu"`.',
    'aws/sagemaker-python-sdk': 'Fixed Local Container mode failure when an S3 input channel points to a single file object instead of a prefix directory.',
    'kirilklein/CausalEstimate': 'Resolved silent NaN / incorrect treatment effect estimations in `Matching._compute_effect` caused by unaligned DataFrame index operations.',
    'imann128/tsauditor': 'Added single-row edge case tests for missing, point, contextual, and stationarity anomaly detection.',
    'MonitorControl/MonitorControl': 'Added troubleshooting documentation for macOS dim screen captures and slider brightness jump behavior.'
}

DISPLAY_NAMES = {
    'protocolbuffers/protobuf': 'Google Protocol Buffers',
    'deepspeedai/DeepSpeed': 'Microsoft DeepSpeed',
    'dmlc/xgboost': 'DMLC XGBoost',
    'onnx/onnx': 'ONNX Reference Runtime',
    'pytorch/vision': 'PyTorch Vision',
    'unit8co/darts': 'Unit8 Darts',
    'awslabs/gluonts': 'AWS GluonTS',
    'meta-pytorch/botorch': 'Meta BoTorch',
    'aws/sagemaker-python-sdk': 'AWS SageMaker SDK',
    'MonitorControl/MonitorControl': 'MonitorControl',
    'kirilklein/CausalEstimate': 'CausalEstimate',
    'imann128/tsauditor': 'tsauditor'
}

# Repositories to exclude from external open-source showcase
EXCLUDED_REPOS = {
    'DataZenSomaiya/14_days_challenge',
    'bhushanasati25/Stevens-QuackHacks'
}

def get_token():
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN') or os.environ.get('METRICS_TOKEN') or os.environ.get('GH_STATS_TOKEN')
    if not token:
        try:
            token = subprocess.check_output(['gh', 'auth', 'token'], text=True).strip()
        except Exception:
            token = None
    return token

def fetch_prs(token):
    query = """
    query {
      search(query: "author:ankitdhandharia is:pr -user:ankitdhandharia -org:hiringfleet", type: ISSUE, first: 100) {
        nodes {
          ... on PullRequest {
            number
            title
            state
            url
            createdAt
            mergedAt
            repository {
              nameWithOwner
              stargazerCount
              isPrivate
            }
          }
        }
      }
    }
    """
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Profile-Readme-Updater'
    }
    if token:
        headers['Authorization'] = f'Bearer {token}'
        
    req = urllib.request.Request(
        'https://api.github.com/graphql',
        data=json.dumps({'query': query}).encode('utf-8'),
        headers=headers
    )
    
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        
    if 'errors' in res:
        raise RuntimeError(f"GraphQL error: {res['errors']}")
        
    return res['data']['search']['nodes']

def clean_pr_title(title):
    cleaned = re.sub(r'^(?:\[[^\]]+\]|\b(?:feat|fix|chore|docs|refactor|ci|test)(?:\([^)]+\))?:)\s*', '', title, flags=re.I)
    cleaned = cleaned.strip()
    if cleaned:
        cleaned = cleaned[0].upper() + cleaned[1:]
    return cleaned

def build_table(nodes):
    repos = defaultdict(list)
    for pr in nodes:
        if pr.get('repository') and not pr['repository'].get('isPrivate'):
            repo_name = pr['repository']['nameWithOwner']
            if repo_name in EXCLUDED_REPOS:
                continue
            if pr['state'] in ('OPEN', 'MERGED'):
                repos[repo_name].append(pr)
                
    def sort_key(item):
        repo_name, pr_list = item
        has_merged = any(p['state'] == 'MERGED' for p in pr_list)
        stars = pr_list[0]['repository']['stargazerCount']
        # Merged repos first (0), then open (1). Within group, sort by stars descending.
        return (0 if has_merged else 1, -stars)
        
    sorted_repos = sorted(repos.items(), key=sort_key)
    
    rows = [
        "| Repo | Stars | PR | Impact |",
        "|:-----|:------|:---|:-------|"
    ]
    
    for repo_name, pr_list in sorted_repos:
        owner, repo_short = repo_name.split('/')
        disp_name = DISPLAY_NAMES.get(repo_name, repo_short)
        stars = pr_list[0]['repository']['stargazerCount']
        star_badge = f'<a href="https://github.com/{repo_name}"><img src="https://img.shields.io/github/stars/{repo_name}?style=flat-square&label=%E2%98%85" alt="Stars"/></a>'
        
        # Sort PRs: merged first, then open, latest number first
        sorted_prs = sorted(pr_list, key=lambda p: (0 if p['state'] == 'MERGED' else 1, -p['number']))
        
        # Build dynamic PR state badges (show up to 2 per repo)
        pr_badges = []
        for p in sorted_prs[:2]:
            p_num = p['number']
            p_url = p['url']
            badge = f'<a href="{p_url}"><img src="https://img.shields.io/github/pulls/detail/state/{repo_name}/{p_num}?style=flat-square&label=%23{p_num}" alt="#{p_num}"/></a>'
            pr_badges.append(badge)
            
        pr_str = '&nbsp;'.join(pr_badges)
        
        # If curated impact is available, use it; otherwise use the cleaned PR title
        impact = CURATED_IMPACTS.get(repo_name)
        if not impact:
            impact = clean_pr_title(sorted_prs[0]['title'])
            
        rows.append(f"| **[{disp_name}](https://github.com/{repo_name})** | {star_badge} | {pr_str} | {impact} |")
        
    return '\n'.join(rows)

def update_readme(table_content, readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = r'(<!-- START_SECTION:contributions -->)(.*?)(<!-- END_SECTION:contributions -->)'
    if re.search(pattern, content, flags=re.DOTALL):
        new_content = re.sub(pattern, f'\\1\n{table_content}\n\\3', content, flags=re.DOTALL)
    else:
        # If markers don't exist yet, insert under ## Open Source Contributions
        table_pattern = r'(## Open Source Contributions[\s\S]*?)(?=\n\n<p align="center">\n  <img src="notable\.svg"|\Z)'
        replacement = f"<!-- START_SECTION:contributions -->\n{table_content}\n<!-- END_SECTION:contributions -->"
        new_content = re.sub(table_pattern, replacement, content)
        
    if new_content != content:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    token = get_token()
    print("Fetching external PRs from GitHub...")
    nodes = fetch_prs(token)
    print(f"Found {len(nodes)} PRs across external repositories.")
    table = build_table(nodes)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(script_dir))
    readme_path = os.path.join(repo_root, 'README.md')
    
    print(f"Updating {readme_path}...")
    changed = update_readme(table, readme_path)
    if changed:
        print("README.md updated with latest contributions!")
    else:
        print("README.md is already up to date.")

if __name__ == '__main__':
    main()
