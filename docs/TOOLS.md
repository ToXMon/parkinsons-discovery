# Tool integrations

Created 2026-09-28. How the additional agent resources plug into the workflow
in docs/WORKFLOW.md.

## Google DeepMind science-skills

Repo: https://github.com/google-deepmind/science-skills

Modular agent skills for genomics, structural biology, cheminformatics, and
literature search, grounding agents in 30+ databases (AlphaGenome, AlphaFold
DB, UniProt, ClinVar, and others). Each skill is a directory with a SKILL.md
(YAML frontmatter + instructions), a scripts/ folder, and optional reference
docs; dependencies resolve through `uv`. AlphaGenome needs an API key.

Use in this project:

- Clone the repo and point any skill-following agent at the relevant skill
  directories. The format matches the common SKILL.md convention, so agents
  that support skills (including local coding agents and AdaL-style
  assistants) can load them directly.
- Highest-value skills for the drylab menu: AlphaGenome (GWAS locus
  prioritization, workflow step 2), structural/AFDB skills (step 4),
  literature-grounding skills for every research pass.
- Keep skill usage behind the same registry rules: outputs are citations and
  candidate priorities, never status changes without a source.

## HuggingFace ML Intern / HuggingChat

Repo: https://github.com/huggingface/ml-intern

Status: ARCHIVED. Hugging Face no longer maintains ML Intern and directs users
to HuggingChat (https://huggingface.co/chat/). Do not build project automation
on the archived CLI.

What is still useful:

- The repo documents an agentic pattern (tool runtime on local files, GPU
  sandbox, doom-loop detection, session tracing) worth borrowing for experiment
  card discipline.
- HuggingChat remains available for ad-hoc model chat and quick experiments.
- For programmatic HF access (datasets, models, Inference Providers), use the
  `huggingface_hub` Python library with a READ token in `.env`
  (see .env.example) rather than the retired CLI.

## HuggingFace MCP server

Endpoints:

- OAuth login: https://huggingface.co/mcp?login
- Authorization header with a READ token: https://huggingface.co/mcp

MCP (Model Context Protocol) lets an agent call HF tools (hub search, dataset
inspection, model cards, spaces) as first-class tools. Connection pattern for
an MCP-capable agent or CLI:

1. Generate a READ token at https://huggingface.co/settings/tokens.
2. Register the server with the agent's MCP config, either via the OAuth URL
   in a browser flow or as a header-authenticated endpoint
   (Authorization: Bearer <READ_TOKEN>).
3. Scope: keep the token READ-only. The project never pushes models or data.
4. Use case in this project: dataset discovery for the drylab menu
   (Perturb-seq, scRNA-seq, ADMET sets) and model discovery
   (protein language models, structure tools) during research passes.

Agents that accept MCP servers include HuggingChat-connected clients, Claude
Code / claude mcp add, and most open agent frameworks. Wire the same endpoint
into whichever agent is driving the experiment; the registry workflow is
agent-agnostic.

## Division of labor

- Biomni Lab: primary research passes with databases and Scientific Review.
- Science-skills-enabled local agent: AlphaGenome/structure/database lookups
  with full CLI control; feeds experiment cards.
- brev.dev: GPU drylab runs (docs/WORKFLOW.md menu).
- HuggingChat / huggingface_hub: quick model experiments, dataset and model
  discovery, MCP-connected hub tools.
