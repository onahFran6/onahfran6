<p align="center">
  <img src="https://raw.githubusercontent.com/onahFran6/onahfran6/main/cards/header.png" alt="Francis Onah: senior software engineer, tech lead, backend and DevOps" width="840" />
</p>

<p align="center">
  Ibadan, Nigeria · remote
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/onahfran6"><img src="https://img.shields.io/badge/LinkedIn-onahfran6-2bbc8a?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://medium.com/@onahfran6"><img src="https://img.shields.io/badge/Medium-@onahfran6-2bbc8a?style=flat-square&logo=medium&logoColor=white" alt="Medium" /></a>
  <a href="mailto:onahfran6@gmail.com"><img src="https://img.shields.io/badge/Email-onahfran6@gmail.com-2bbc8a?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://medium.com/@onahfran6/how-i-prepared-for-the-ckad-and-scored-93-f0c0cfde77ab"><img src="https://img.shields.io/badge/CKAD-certified-2bbc8a?style=flat-square&logo=kubernetes&logoColor=whte" alt="Certified Kubernetes Application Developer" /></a>
</p>

## About

I'm a senior software engineer and tech lead with six years of building production backends: the services, the infrastructure under them and the pipelines that ship them, with React or Next.js on the front when a team needs it. I've done that in fintech, health tech, edtech and consumer apps, for teams in Nigeria, Singapore and the US. My full work history is on [LinkedIn](https://www.linkedin.com/in/onahfran6).

As contract tech lead at [Stroll](https://www.linkedin.com/company/stroll-dating), a voice messaging and matching app, I designed the NestJS microservices on AWS (ECS, Lambda, DynamoDB), provisioned everything with Terraform, and set up CI/CD with GitHub Actions and monitoring with Prometheus and Grafana. That work cut response times by up to 30%, infrastructure cost by 25% and deployment time by about 40%.

I'm a Certified Kubernetes Application Developer (CKAD) and a mentor at Tech4Dev. On my own time I build developer tools: hands-on Kubernetes practice, and local-first search and storage in Rust and Go. Away from the keyboard, I play a lot of chess.

## Now

- Building [ClusterDrill](https://github.com/onahFran6/clusterdrill) and [ClusterDrill Lab](https://github.com/onahFran6/clusterdrill-lab), an open-source CKAD practice platform and its AWS lab
- Mentoring early-career software engineers at Tech4Dev
- Tuning [aperture](https://github.com/onahFran6/aperture)'s hybrid search (BM25 + HNSW)

## Projects

<p align="center">
  <a href="https://github.com/onahFran6/clusterdrill"><img src="https://raw.githubusercontent.com/onahFran6/onahfran6/main/cards/clusterdrill.png" alt="ClusterDrill: CKAD practice graded by a live cluster" width="420" /></a>
  <a href="https://github.com/onahFran6/clusterdrill-lab"><img src="https://raw.githubusercontent.com/onahFran6/onahfran6/main/cards/clusterdrill-lab.png" alt="ClusterDrill Lab: disposable Kubernetes lab on AWS" width="420" /></a>
</p>

<p align="center">
  <a href="https://github.com/onahFran6/aperture"><img src="https://raw.githubusercontent.com/onahFran6/onahfran6/main/cards/aperture.png" alt="aperture: offline code search" width="420" /></a>
  <a href="https://github.com/onahFran6/atlasDB"><img src="https://raw.githubusercontent.com/onahFran6/onahfran6/main/cards/atlasdb.png" alt="atlasDB: local-first key-value store" width="420" /></a>
</p>

### [ClusterDrill](https://github.com/onahFran6/clusterdrill)

CKAD practice that grades you against a real cluster, not a quiz.

More than 600 hands-on questions, a timed mock-exam mode and a terminal in the browser. Each question seeds a broken namespace, and `check.sh` grades the live state. FastAPI, ttyd and tmux, shipped as a Helm chart. [Write-up](https://medium.com/@onahfran6/building-clusterdrill-a-ckad-practice-platform-graded-by-the-cluster-itself-45afeb175af5)

### [ClusterDrill Lab](https://github.com/onahFran6/clusterdrill-lab)

A throwaway Kubernetes cluster on AWS, built for practising the way the exam feels.

Terraform creates the VPC and EC2 nodes, and a cloud-agnostic bootstrap installs kubeadm, containerd and Cilium over SSH. Optional noVNC desktop, ClusterDrill and Headlamp. [Write-up](https://medium.com/@onahfran6/building-clusterdrill-lab-a-disposable-exam-realistic-kubernetes-lab-on-aws-c52edf96e5f5)

### [aperture](https://github.com/onahFran6/aperture)

Offline code search. You can look through a private repo by keyword or by meaning, without uploading the tree anywhere.

It walks the repo, chunks with tree-sitter, indexes with BM25 and HNSW, then fuses the rankings (RRF). CLI and TUI, all in Rust.

### [atlasDB](https://github.com/onahFran6/atlasDB)

A small embedded key-value store for apps that need to keep working offline.

WAL with fsync so a crash does not eat writes. Vector clocks and P2P sync when you come back online. Go, with tests.

## Writing

- [How I Prepared for the CKAD and Scored 93%](https://medium.com/@onahfran6/how-i-prepared-for-the-ckad-and-scored-93-f0c0cfde77ab)
- [Building ClusterDrill: A CKAD Practice Platform Graded by the Cluster Itself](https://medium.com/@onahfran6/building-clusterdrill-a-ckad-practice-platform-graded-by-the-cluster-itself-45afeb175af5)
- [Building ClusterDrill Lab: A Disposable, Exam-Realistic Kubernetes Lab on AWS](https://medium.com/@onahfran6/building-clusterdrill-lab-a-disposable-exam-realistic-kubernetes-lab-on-aws-c52edf96e5f5)

More on [Medium](https://medium.com/@onahfran6).

## Tools

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,js,nodejs,nestjs,react,nextjs,go,rust,py,fastapi,graphql&perline=11" alt="TypeScript, JavaScript, Node.js, NestJS, React, Next.js, Go, Rust, Python, FastAPI, GraphQL" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=aws,terraform,kubernetes,docker,githubactions,prometheus,grafana,nginx,linux&perline=9" alt="AWS, Terraform, Kubernetes, Docker, GitHub Actions, Prometheus, Grafana, Nginx, Linux" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=postgres,mongodb,redis,dynamodb,mysql&perline=5" alt="PostgreSQL, MongoDB, Redis, DynamoDB, MySQL" />
</p>
