from pathlib import Path

path = Path("index.html")
text = path.read_text(encoding="utf-8")


def replace_once(old: str, new: str, label: str) -> None:
    global text
    if old not in text:
        raise SystemExit(f"Could not find expected {label} block; refusing to modify index.html")
    text = text.replace(old, new, 1)


replace_once(
    '<meta name="description" content="Lyoneh Gbojueh — Computer Science graduate building software, IT support tools, cloud projects, and secure systems." />',
    '<meta name="description" content="Lyoneh Gbojueh — Computer Science graduate building full-stack software, evidence-first support tools, secure systems, and cloud-ready infrastructure." />',
    "meta description",
)

replace_once(
    """      Computer Science graduate building full-stack applications,
      support tools, cloud-ready infrastructure, and secure systems.
      Explore my work through the interactive 3D project network.""",
    """      Computer Science graduate building full-stack applications,
      evidence-first support tools, secure systems, and cloud-ready infrastructure.
      Explore my strongest engineering work through the interactive 3D project network.""",
    "hero description",
)

replace_once(
    """      <small>
        Full-Stack DevOps Project
      </small>

      <h3>
        Docker Deployment Lab
      </h3>

      <p>
        Multi-container Docker deployment lab with Nginx,
        PostgreSQL, Redis, and an interactive monitoring dashboard.
      </p>

      <div class="tags">
        <span class="tag">Docker</span>
        <span class="tag">Nginx</span>
        <span class="tag">PostgreSQL</span>
      </div>

      <a
        href="https://github.com/lgbojueh/docker-deployment-lab"
        target="_blank"
        rel="noopener"
        class="project-pop-link"
      >
        View repository on GitHub →
      </a>""",
    """      <small>
        Evidence-First Support Engineering
      </small>

      <h3>
        SignalDesk AI
      </h3>

      <p>
        Full-stack technical support platform that classifies incidents,
        retrieves relevant knowledge, scores confidence and severity,
        and produces cited troubleshooting workflows with escalation logic.
      </p>

      <div class="tags">
        <span class="tag">React</span>
        <span class="tag">FastAPI</span>
        <span class="tag">Python</span>
        <span class="tag">CI/CD</span>
      </div>

      <a
        href="https://github.com/lgbojueh/signaldesk-ai"
        target="_blank"
        rel="noopener"
        class="project-pop-link"
      >
        View SignalDesk on GitHub →
      </a>""",
    "default globe project card",
)

replace_once(
    """    A collection of web applications, IT support tools,
    security projects, command-line applications,
    and infrastructure labs.""",
    """    Selected projects demonstrating full-stack development,
    support engineering, security, systems programming,
    and production-minded infrastructure.""",
    "selected work description",
)

signaldesk = '''window.portfolioProjects = [

  {
    title: "SignalDesk AI",
    label: "Evidence-First Support Platform",

    description:
      "Full-stack support engineering platform that classifies incidents, retrieves relevant knowledge, scores confidence and severity, and returns cited troubleshooting workflows with human-escalation logic.",

    tech: [
      "React",
      "TypeScript",
      "FastAPI",
      "Python",
      "SQL",
      "GitHub Actions"
    ],

    repo:
      "https://github.com/lgbojueh/signaldesk-ai",

    lat: 37.7749,
    lon: -122.4194,
    color: 0x8b5cf6
  },
'''

replace_once(
    "window.portfolioProjects = [\n",
    signaldesk,
    "project data start",
)

replace_once(
    """        I am seeking early-career roles in software engineering,
        IT support, cloud computing, cybersecurity,
        or technical operations.""",
    """        I am seeking early-career software engineering and full-stack roles,
        with additional strengths in support tooling, security,
        systems, and cloud-ready infrastructure.""",
    "career focus",
)

replace_once(
    """      I am open to software engineering,
      IT support, cloud, cybersecurity,
      and technical operations opportunities.""",
    """      I am open to early-career software engineering,
      full-stack development, and technical product roles
      where I can build, troubleshoot, and grow.""",
    "contact focus",
)

path.write_text(text, encoding="utf-8")
print("Portfolio updated with SignalDesk AI.")
