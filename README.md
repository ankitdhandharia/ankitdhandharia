<!-- ====================== HEADER BANNER ====================== -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:378ADD,100:0045A5&height=200&section=header&text=Ankit%20Dhandharia&fontColor=ffffff&fontSize=52&fontAlignY=38&desc=Distributed%20Systems%20%C2%B7%20Data%20Platforms%20%C2%B7%20ML%20Infrastructure&descAlignY=60&descSize=18" width="100%" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&pause=1000&color=378ADD&center=true&vCenter=true&width=680&lines=Distributed+Systems+%E2%80%A2+Data+Platforms+%E2%80%A2+ML+Infra;Building+High-Throughput+Pipelines+%7C+Kafka+%7C+Spark+%7C+dbt;Contributing+Upstream+to+Protobuf%2C+DeepSpeed%2C+ONNX%2C+Darts;AWS+Certified+Data+Engineer+%E2%80%93+Associate;MSCS+%40+Stevens+Institute+of+Technology+%F0%9F%8E%93" alt="Typing SVG" />
</p>

<!-- ====================== SOCIAL BADGES ====================== -->
<p align="center">
  <a href="https://ankitdhandharia.com"><img src="https://img.shields.io/badge/Portfolio-378ADD?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio" /></a>&nbsp;
  <a href="https://linkedin.com/in/ankit-dhandharia/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>&nbsp;
  <a href="mailto:ankitdhandharia21@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>&nbsp;
  <a href="https://www.credly.com/badges/2d86b01c-3459-4bb4-ad39-4cc492678060"><img src="https://img.shields.io/badge/AWS_Certified-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS Certified" /></a>&nbsp;
  <img src="https://komarev.com/ghpvc/?username=ankitdhandharia&label=Profile+Views&color=378ADD&style=for-the-badge" alt="Profile Views" />
</p>

<br/>

<!-- ====================== ABOUT ====================== -->
## <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="28"> About Me

I am a software engineer focused on **distributed systems**, **data platforms**, and **machine learning infrastructure**. I enjoy tackling problems where correctness and runtime performance matter most: eliminating multithreaded race conditions, resolving execution graph edge cases, and building high-throughput data pipelines that remain reliable under heavy loads.

- 🎓 **M.S. Computer Science** @ **Stevens Institute of Technology** (Hoboken, NJ — GPA **3.71 / 4.0** · [Digital Degree](https://www.parchment.com/lp/award/e991230d-435f-4a4f-90e8-8809f734e43a))
- ☁️ **AWS Certified Data Engineer – Associate** ([Verify on Credly](https://www.credly.com/badges/2d86b01c-3459-4bb4-ad39-4cc492678060))
- ⚙️ **Systems & Distributed Computing**: Concurrency safety, race-condition elimination, execution graph optimization, and low-latency communication runtimes.
- 🌊 **Data Engineering & Lakehouses**: Production-grade Medallion architecture (Snowflake + dbt Core + S3), incremental loading, SCD Type 2 snapshots, and streaming pipelines (Kafka + Spark).
- 🔬 **Upstream Open-Source Engineering**: Actively resolving runtime edge cases and bugs across foundational repositories including Google Protocol Buffers, Microsoft DeepSpeed, ONNX, and PyTorch Vision.
- 🌐 **Portfolio & Architecture Write-ups** → **[ankitdhandharia.com](https://ankitdhandharia.com)**

<br/>

---

<!-- ====================== UPSTREAM OPEN SOURCE ====================== -->
## ⚡ Upstream Open-Source Contributions

Real-time snapshot of public pull requests and upstream engineering contributions across external ecosystems, auto-updated via GitHub Actions:

<p align="center">
  <img src="./open-source-showcase.svg" alt="Upstream Open Source Ecosystem" width="100%" />
</p>

### 🧠 Machine Learning Runtimes & Distributed Systems

- **[ONNX Reference Runtime](https://github.com/onnx/onnx)** `★ 21.6k` · [![PR #8599](https://img.shields.io/github/pulls/detail/state/onnx/onnx/8599?style=flat-square&label=%238599)](https://github.com/onnx/onnx/pull/8599)
  > Handled legacy Resize inputs in reference implementation and preserved exact nearest-neighbor sub-pixel coordinate roundings across opset 10/11 transitions.

- **[Microsoft DeepSpeed](https://github.com/deepspeedai/DeepSpeed)** `★ 43.2k` · [![PR #8631](https://img.shields.io/github/pulls/detail/state/deepspeedai/DeepSpeed/8631?style=flat-square&label=%238631)](https://github.com/deepspeedai/DeepSpeed/pull/8631)
  > Fixed AutoSP test suite expecting LLM decoder attention layers to be auto-wrapped with `DistributedAttention`, aligning tests with the intentional sequence parallelism operator architecture.

- **[PyTorch Vision](https://github.com/pytorch/vision)** `★ 18.0k` · [![PR #9677](https://img.shields.io/github/pulls/detail/state/pytorch/vision/9677?style=flat-square&label=%239677)](https://github.com/pytorch/vision/pull/9677)
  > Guarded reference `evaluate()` sample-count checks against uninitialized default process groups when benchmarks run in standalone non-distributed mode.

- **[DMLC XGBoost](https://github.com/dmlc/xgboost)** `★ 28.9k` · [![PR #12613](https://img.shields.io/github/pulls/detail/state/dmlc/xgboost/12613?style=flat-square&label=%2312613)](https://github.com/dmlc/xgboost/pull/12613)
  > Added strict Python type annotations to config and tree regularization test suites and enabled mypy CI verification.

### 📊 Time-Series, Bayesian Optimization & Statistical Engines

- **[Unit8 Darts](https://github.com/unit8co/darts)** `★ 9.6k` · [![Merged #3217](https://img.shields.io/badge/%233217-Merged-2ea44f?style=flat-square)](https://github.com/unit8co/darts/pull/3217) [![Merged #3210](https://img.shields.io/badge/%233210-Merged-2ea44f?style=flat-square)](https://github.com/unit8co/darts/pull/3210)
  > **Merged**: Resolved multithreaded race condition where `ModelMeta.__call__` stored creation arguments in class-level attributes, preventing collisions during parallel Optuna sweeps (`n_jobs>1`). Also documented `window` parameter in `CauchyNLLScorer`.

- **[Meta BoTorch](https://github.com/meta-pytorch/botorch)** `★ 3.6k` · [![PR #3411](https://img.shields.io/github/pulls/detail/state/meta-pytorch/botorch/3411?style=flat-square&label=%233411)](https://github.com/meta-pytorch/botorch/pull/3411)
  > Introduced pluggable `cat_kernel_factory` in `MixedSingleTaskGP` to support domain-specific categorical kernels alongside continuous dimensions.

- **[AWS GluonTS](https://github.com/awslabs/gluonts)** `★ 5.2k` · [![PR #3351](https://img.shields.io/github/pulls/detail/state/awslabs/gluonts/3351?style=flat-square&label=%233351)](https://github.com/awslabs/gluonts/pull/3351)
  > Prevented unintended CUDA context initialization by enforcing CPU predictor placement when training with `accelerator="cpu"`.

- **[CausalEstimate](https://github.com/kirilklein/CausalEstimate)** · [![Merged #148](https://img.shields.io/badge/%23148-Merged-2ea44f?style=flat-square)](https://github.com/kirilklein/CausalEstimate/pull/148) & **[tsauditor](https://github.com/imann128/tsauditor)** · [![Merged #74](https://img.shields.io/badge/%2374-Merged-2ea44f?style=flat-square)](https://github.com/imann128/tsauditor/pull/74)
  > **Merged**: Fixed unaligned DataFrame index in `Matching._compute_effect` that caused silent NaN calculations; added single-row anomaly edge-case test suites.

### 🔌 Core Protocols & Cloud Tooling

- **[Google Protocol Buffers](https://github.com/protocolbuffers/protobuf)** `★ 72.1k` · [![PR #30114](https://img.shields.io/github/pulls/detail/state/protocolbuffers/protobuf/30114?style=flat-square&label=%2330114)](https://github.com/protocolbuffers/protobuf/pull/30114)
  > Included duplicate collision key in C# `MapField.Add` exception message to accelerate debugging in downstream cloud logging services.

- **[AWS SageMaker Python SDK](https://github.com/aws/sagemaker-python-sdk)** `★ 2.3k` · [![PR #6430](https://img.shields.io/github/pulls/detail/state/aws/sagemaker-python-sdk/6430?style=flat-square&label=%236430)](https://github.com/aws/sagemaker-python-sdk/pull/6430)
  > Fixed Local Container mode failure when an S3 input channel points to an individual file object instead of a prefix directory.

- **[MonitorControl](https://github.com/MonitorControl/MonitorControl)** `★ 34.5k` · [![PR #1913](https://img.shields.io/github/pulls/detail/state/MonitorControl/MonitorControl/1913?style=flat-square&label=%231913)](https://github.com/MonitorControl/MonitorControl/pull/1913)
  > Documented troubleshooting resolutions for macOS dim screen capture conflicts and slider brightness jumps.

<p align="center">
  <a href="https://github.com/pulls?q=is%3Apr+author%3Aankitdhandharia+-user%3Aankitdhandharia">
    <img src="https://img.shields.io/badge/GitHub-View_All_Upstream_PRs-378ADD?style=for-the-badge&logo=github&logoColor=white" alt="View All PRs" />
  </a>
</p>

<br/>

---

<!-- ====================== FEATURED SYSTEMS ====================== -->
## 🛠 Featured Systems & Architecture

<table>
<tr>
<td width="50%" valign="top">

### 🏔 [Medallion Data Lakehouse](https://github.com/ankitdhandharia/AWS_DBT_Snowflake)
**`dbt Core` `Snowflake` `AWS S3` `Jinja`**

End-to-end cloud data warehouse implementing the **Bronze → Silver → Gold** architecture on an Airbnb dataset.
- Incremental loading + **SCD Type 2** snapshots for point-in-time dimensional accuracy
- Metadata-driven Gold layer with custom **dbt Jinja macros**
- Automated schema validation & freshness assertions — **40% compute cost cut** via incremental materialization

</td>
<td width="50%" valign="top">

### ⚡ [Autonomous Multi-Source Aggregator](https://github.com/hiringfleet/HiringFleet---Tech-Professional-Events-Aggregator)
**`TypeScript` `Node.js` `Distributed Ingestion` `APIs`**

Distributed event ingestion and normalization platform integrating 8+ external sources (Luma, Meetup, Ticketmaster, Pretalx, Devpost, Kaggle).
- Unified schema normalization and cross-platform deduplication
- Zero-auth data adapters for open-data event syndication
- Click-to-recommendation feedback loop with low-latency dispatch

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🛡 [Deterministic LLM Model Gateway](https://github.com/hiringfleet/HiringFleet-Portal-Resume-Optimizer)
**`FastAPI` `Python` `OpenRouter` `Security Guardrails`**

Multi-tier LLM gateway with deterministic model dispatch (GPT-4o-mini & DeepSeek-V3.2) and token budgeting.
- Shared daily cost/token caps across concurrent execution engines
- Defense-in-depth security guardrails mitigating SSRF, prompt injection, and DoS attacks
- Section-scoped semantic prompting for deterministic outputs

</td>
<td width="50%" valign="top">

### 🤖 [Progressive Hybrid RAG Pipeline](https://github.com/ankitdhandharia/RAG_Project)
**`LangChain` `ChromaDB` `HuggingFace` `Vector Embeddings`**

Modular Retrieval-Augmented Generation system with dense embeddings and persistent vector indexing.
- Zero cloud API dependency using local HuggingFace embeddings (384-dim)
- Persistent **ChromaDB** vector store with sub-second retrieval across 400+ page documents
- Clean OOP architecture ready for high-throughput inference

</td>
</tr>
</table>

<p align="center"><a href="https://github.com/ankitdhandharia?tab=repositories">→ Browse all repositories</a></p>

<br/>

---

<!-- ====================== TECH STACK ====================== -->
## 🛠 Technical Toolkit

<div align="center">

**Languages & Systems**

<img src="https://skillicons.dev/icons?i=python,cpp,ts,js,bash,go&theme=dark" />

**Data Engineering & Big Data**

<img src="https://skillicons.dev/icons?i=apache,kafka&theme=dark" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apachespark/apachespark-original.svg" width="48" title="Spark" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apacheairflow/apacheairflow-original.svg" width="48" title="Airflow" />
<img src="https://raw.githubusercontent.com/gilbarbara/logos/main/logos/dbt.svg" width="46" title="dbt" />
<img src="https://www.vectorlogo.zone/logos/snowflake/snowflake-icon.svg" width="48" title="Snowflake" />
<img src="https://www.vectorlogo.zone/logos/databricks/databricks-icon.svg" width="46" title="Databricks" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/hadoop/hadoop-original.svg" width="48" title="Hadoop" />

**Cloud & DevOps**

<img src="https://skillicons.dev/icons?i=aws,gcp,docker,kubernetes,terraform,githubactions,linux,git&theme=dark" />

**AI / ML & Frameworks**

<img src="https://skillicons.dev/icons?i=pytorch,tensorflow,sklearn&theme=dark" />
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" width="46" title="pandas" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="48" title="NumPy" />
<img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" width="46" title="HuggingFace" />

**Databases & Backend**

<img src="https://skillicons.dev/icons?i=postgres,mysql,sqlite,mongodb,redis,fastapi&theme=dark" />

</div>

<br/>

---

<!-- ====================== EDUCATION & CREDENTIALS ====================== -->
## 🎓 Education & Credentials

<table>
  <tr>
    <td width="50%" align="center" valign="top">
      <br/>
      <a href="https://www.parchment.com/lp/award/e991230d-435f-4a4f-90e8-8809f734e43a">
        <img src="./assets/stevens-logo.png" height="85" alt="Stevens Institute of Technology" />
      </a>
      <br/><br/>
      <h3>Stevens Institute of Technology</h3>
      <b>M.S. in Computer Science</b><br/>
      <sub>Hoboken, NJ · Sep 2024 – May 2026</sub><br/>
      <p>GPA: <b>3.71 / 4.0</b></p>
      <sub>Distributed Systems · Machine Learning · Cloud Computing · Advanced Algorithms</sub>
      <br/><br/>
      <a href="https://www.parchment.com/lp/award/e991230d-435f-4a4f-90e8-8809f734e43a"><b>🎓 View Digital Degree (Parchment) »</b></a>
      <br/><br/>
    </td>
    <td width="50%" align="center" valign="top">
      <br/>
      <a href="https://www.credly.com/badges/2d86b01c-3459-4bb4-ad39-4cc492678060">
        <img src="https://images.credly.com/size/340x340/images/e5c85d7f-4e50-431e-b5af-fa9d9b0596e7/image.png" height="85" alt="AWS Certified Data Engineer – Associate" />
      </a>
      <br/><br/>
      <h3>Amazon Web Services</h3>
      <b>AWS Certified Data Engineer – Associate</b><br/>
      <sub>Issued by Amazon Web Services Training &amp; Certification</sub><br/>
      <p>Active Credential: <b>March 2026</b></p>
      <a href="https://www.credly.com/badges/2d86b01c-3459-4bb4-ad39-4cc492678060"><b>🔗 Verify on Credly »</b></a>
      <br/><br/>
    </td>
  </tr>
</table>

<br/>

---

<!-- ====================== GITHUB ACTIVITY ====================== -->
## 📊 GitHub Activity

<p align="center">
  <img src="https://streak-stats.demolab.com?user=ankitdhandharia&theme=github-dark-blue&hide_border=true&background=0D1117&ring=378ADD&fire=378ADD&currStreakLabel=378ADD" height="195" alt="Contribution Streak" />
</p>

<p align="center">
  <img src="https://gh-readme-activity-graph.vercel.app/graph?username=ankitdhandharia&theme=react-dark&hide_border=true&area=true" width="100%" alt="Activity Graph" />
</p>

<br/>

<!-- ====================== FOOTER ====================== -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0045A5,100:378ADD&height=120&section=footer" width="100%" />
</p>

<p align="center">
  <a href="https://ankitdhandharia.com"><b>ankitdhandharia.com</b></a>
</p>
