# Francis Onah

Tech lead on backends and cloud. I also build local-first tools in Rust and Go.

[LinkedIn](https://www.linkedin.com/in/onahfran6) · [onahfran6@gmail.com](mailto:onahfran6@gmail.com)

## About

Six years as a software engineer. The titles have been tech lead, backend, full stack, and DevOps, depending on the team. The work is the same: APIs and cloud infra that stay up, cost less to run, and do not take forever to ship.

Most days that is TypeScript and NestJS, sometimes Go. AWS and Terraform for the platform, Postgres and Redis for data, Prometheus and Grafana when something is slow. I have also done payment integrations (Stripe, Paystack, Flutterwave).

On my own time I write local-first tools in Rust and Go. Search and storage that run on your machine, so private code does not have to leave it.

## Now

- Contract tech lead on a voice messaging product: NestJS services on AWS, infra in Terraform
- [aperture](https://github.com/onahFran6/aperture) and [atlasDB](https://github.com/onahFran6/atlasDB) in public
- Studying Kubernetes (CKAD) and still tweaking hybrid search (BM25 + HNSW)

## Projects

### [aperture](https://github.com/onahFran6/aperture)

Offline code search. You can look through a private repo by keyword or by meaning, without uploading the tree anywhere.

It walks the repo, chunks with tree-sitter, indexes with BM25 and HNSW, then fuses the rankings (RRF). CLI and TUI, all in Rust.

`Rust` · `tree-sitter` · `MIT`

### [atlasDB](https://github.com/onahFran6/atlasDB)

A small embedded key-value store for apps that need to keep working offline.

WAL with fsync so a crash does not eat writes. Vector clocks and P2P sync when you come back online. Go, with tests.

`Go` · `MIT`

<details>
<summary>Other repos</summary>

| Project | Note |
|---------|------|
| [code-editor-backend](https://github.com/onahFran6/code-editor-backend) | Collaborative editor backend, TypeScript |
| [e-commerce-microservices](https://github.com/onahFran6/e-commerce-microservices) | Microservices sketch |
| [onahrestaulServer](https://github.com/onahFran6/onahrestaulServer) | Terraform for an API |

</details>

## What I work with

- Backend: TypeScript, NestJS, Node.js, Go
- Cloud: AWS, Terraform, Docker, Kubernetes, GitHub Actions
- Data and ops: PostgreSQL, Redis, Prometheus, Grafana
- Payments: Stripe, Paystack, Flutterwave
- Also: Rust, Python, Linux

[onahfran6@gmail.com](mailto:onahfran6@gmail.com) · [LinkedIn](https://www.linkedin.com/in/onahfran6)
