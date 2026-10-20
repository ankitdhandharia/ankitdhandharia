#!/usr/bin/env python3
"""
Custom SVG Generator for Ankit Dhandharia's Upstream Open Source Showcase.
Fetches real-time GitHub PR and repository data and generates a clean,
bespoke, responsive dark-mode SVG card for the profile README.
"""

import os
import json
import subprocess
import urllib.request
from datetime import datetime, timezone

CURATED_DATA = {
    'unit8co/darts': {
        'name': 'Unit8 Darts',
        'desc': 'Multithreaded Optuna race-condition fix in _model_call',
        'category': 'Time-Series & Forecasting'
    },
    'protocolbuffers/protobuf': {
        'name': 'Google Protocol Buffers',
        'desc': 'C# MapField duplicate collision key in exception message',
        'category': 'Serialization & Systems'
    },
    'deepspeedai/DeepSpeed': {
        'name': 'Microsoft DeepSpeed',
        'desc': 'AutoSP test alignment for LLM attention layer wrapping',
        'category': 'Distributed ML'
    },
    'onnx/onnx': {
        'name': 'ONNX Runtime',
        'desc': 'Legacy Resize input handling & sub-pixel precision',
        'category': 'ML Runtimes'
    },
    'pytorch/vision': {
        'name': 'PyTorch Vision',
        'desc': 'Guard uninitialized distributed process group in evaluate()',
        'category': 'Computer Vision'
    },
    'dmlc/xgboost': {
        'name': 'DMLC XGBoost',
        'desc': 'Type annotations for config & tree regularization tests',
        'category': 'ML Compilers'
    },
    'meta-pytorch/botorch': {
        'name': 'Meta BoTorch',
        'desc': 'Pluggable cat_kernel_factory for MixedSingleTaskGP',
        'category': 'Bayesian Optimization'
    },
    'awslabs/gluonts': {
        'name': 'AWS GluonTS',
        'desc': 'Strict CPU predictor enforcement on GPU environments',
        'category': 'Time-Series & ML'
    },
    'aws/sagemaker-python-sdk': {
        'name': 'AWS SageMaker SDK',
        'desc': 'Local container mode single-file S3 input resolution',
        'category': 'Cloud & ML Infra'
    },
    'kirilklein/CausalEstimate': {
        'name': 'CausalEstimate',
        'desc': 'Index alignment fix in Matching estimator for unbiased effect',
        'category': 'Causal Inference'
    }
}

def get_token():
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_STATS_TOKEN') or os.environ.get('METRICS_TOKEN')
    if not token:
        try:
            token = subprocess.check_output(['gh', 'auth', 'token'], text=True).strip()
        except Exception:
            token = None
    return token

def fetch_data(token):
    query = """
    query {
      search(query: "author:ankitdhandharia is:pr -user:ankitdhandharia -org:hiringfleet", type: ISSUE, first: 100) {
        nodes {
          ... on PullRequest {
            number
            title
            state
            url
            repository {
              nameWithOwner
              stargazerCount
            }
          }
        }
      }
    }
    """
    headers = {'Content-Type': 'application/json', 'User-Agent': 'Profile-SVG-Builder'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
        
    req = urllib.request.Request(
        'https://api.github.com/graphql',
        data=json.dumps({'query': query}).encode('utf-8'),
        headers=headers
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        
    nodes = res['data']['search']['nodes']
    repos = {}
    merged_count = 0
    open_count = 0
    
    for pr in nodes:
        if not pr.get('repository'):
            continue
        rname = pr['repository']['nameWithOwner']
        if rname in ('DataZenSomaiya/14_days_challenge', 'bhushanasati25/Stevens-QuackHacks'):
            continue
        if rname not in repos:
            repos[rname] = {
                'stars': pr['repository']['stargazerCount'],
                'prs': []
            }
        repos[rname]['prs'].append(pr)
        if pr['state'] == 'MERGED':
            merged_count += 1
        elif pr['state'] == 'OPEN':
            open_count += 1
            
    total_stars = sum(r['stars'] for r in repos.values())
    return repos, total_stars, merged_count, open_count

def escape_xml(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

def generate_svg(repos, total_stars, merged_count, open_count, output_path):
    width = 850
    height = 400
    now_str = datetime.now(timezone.utc).strftime('%b %d, %Y')
    
    # Select top 8 notable repos sorted by stars (with merged prioritization)
    sorted_repos = sorted(
        repos.items(),
        key=lambda x: (0 if any(p['state'] == 'MERGED' for p in x[1]['prs']) else 1, -x[1]['stars'])
    )[:8]
    
    cards_svg = []
    # 2 columns x 4 rows
    col_width = 390
    card_height = 54
    start_x = 25
    start_y = 135
    gap_x = 20
    gap_y = 10
    
    for i, (repo_name, info) in enumerate(sorted_repos):
        col = i % 2
        row = i // 2
        cx = start_x + col * (col_width + gap_x)
        cy = start_y + row * (card_height + gap_y)
        
        meta = CURATED_DATA.get(repo_name, {
            'name': repo_name.split('/')[-1],
            'desc': info['prs'][0]['title'][:45] + '...',
            'category': 'Open Source'
        })
        
        has_merged = any(p['state'] == 'MERGED' for p in info['prs'])
        status_label = "MERGED" if has_merged else "OPEN"
        status_color = "#2ea44f" if has_merged else "#a371f7"
        status_bg = "rgba(46, 164, 79, 0.15)" if has_merged else "rgba(163, 113, 247, 0.15)"
        
        stars_formatted = f"{info['stars']:,}" if info['stars'] < 1000 else f"{info['stars']/1000:.1f}k"
        
        card = f"""
        <g transform="translate({cx}, {cy})">
          <rect width="{col_width}" height="{card_height}" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1"/>
          
          <!-- Repo Name -->
          <text x="14" y="22" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="13" font-weight="600" fill="#58a6ff">{escape_xml(meta['name'])}</text>
          
          <!-- Stars pill -->
          <rect x="{col_width - 130}" y="10" width="52" height="18" rx="4" fill="#21262d"/>
          <text x="{col_width - 104}" y="23" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="10" font-weight="600" fill="#e3b341">★ {stars_formatted}</text>
          
          <!-- Status pill -->
          <rect x="{col_width - 70}" y="10" width="56" height="18" rx="4" fill="{status_bg}" stroke="{status_color}" stroke-width="0.75"/>
          <text x="{col_width - 42}" y="23" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="10" font-weight="700" fill="{status_color}">{status_label}</text>
          
          <!-- Impact summary -->
          <text x="14" y="42" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="11" fill="#8b949e">{escape_xml(meta['desc'][:54])}</text>
        </g>
        """
        cards_svg.append(card)
        
    cards_rendered = '\n'.join(cards_svg)
    stars_k = f"{total_stars/1000:.0f}K+" if total_stars >= 1000 else str(total_stars)
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none">
  <defs>
    <linearGradient id="header-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#378ADD" />
      <stop offset="100%" stop-color="#58a6ff" />
    </linearGradient>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117" />
      <stop offset="100%" stop-color="#0b0e14" />
    </linearGradient>
  </defs>

  <!-- Container Box -->
  <rect width="{width}" height="{height}" rx="12" fill="url(#bg-grad)" stroke="#30363d" stroke-width="1.5" />

  <!-- Card Header -->
  <g transform="translate(25, 24)">
    <!-- Pulse icon -->
    <circle cx="8" cy="8" r="5" fill="#378ADD" opacity="0.3"/>
    <circle cx="8" cy="8" r="3" fill="#58a6ff"/>
    
    <!-- Title -->
    <text x="24" y="13" font-family="'Fira Code', -apple-system, monospace" font-size="15" font-weight="700" fill="url(#header-grad)" letter-spacing="0.5">UPSTREAM OPEN-SOURCE ECOSYSTEM</text>
    <text x="24" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="11" fill="#8b949e">Active contributions across foundational runtimes, compilers &amp; distributed frameworks</text>
    
    <!-- Sync badge -->
    <rect x="{width - 220}" y="0" width="170" height="24" rx="12" fill="#161b22" stroke="#30363d" stroke-width="1"/>
    <circle cx="{width - 206}" cy="12" r="3" fill="#2ea44f"/>
    <text x="{width - 194}" y="16" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="11" font-weight="500" fill="#c9d1d9">Auto-synced • 6h cycle</text>
  </g>

  <!-- Metric Tiles -->
  <g transform="translate(25, 68)">
    <!-- Tile 1 -->
    <rect x="0" y="0" width="250" height="52" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1"/>
    <text x="18" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="20" font-weight="700" fill="#f0f6fc">{stars_k}</text>
    <text x="18" y="41" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="11" fill="#8b949e">Stars Across Upstream Repos</text>

    <!-- Tile 2 -->
    <rect x="275" y="0" width="250" height="52" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1"/>
    <text x="293" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="20" font-weight="700" fill="#f0f6fc">{len(repos)} Codebases</text>
    <text x="293" y="41" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="11" fill="#8b949e">Major Projects Contributed To</text>

    <!-- Tile 3 -->
    <rect x="550" y="0" width="250" height="52" rx="8" fill="#161b22" stroke="#30363d" stroke-width="1"/>
    <text x="568" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="20" font-weight="700" fill="#f0f6fc">{merged_count} Merged <tspan fill="#8b949e" font-size="15" font-weight="400">·</tspan> {open_count} Open</text>
    <text x="568" y="41" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="11" fill="#8b949e">External Pull Requests</text>
  </g>

  <!-- Repo Cards Grid -->
  {cards_rendered}

</svg>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg.strip())
    print(f"Generated {output_path} successfully.")

def main():
    token = get_token()
    print("Fetching repository and PR metrics from GitHub...")
    repos, total_stars, merged_count, open_count = fetch_data(token)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(script_dir))
    output_path = os.path.join(repo_root, 'open-source-showcase.svg')
    
    generate_svg(repos, total_stars, merged_count, open_count, output_path)

if __name__ == '__main__':
    main()
