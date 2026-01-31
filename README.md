<p align="center">
  <img src="https://img.shields.io/badge/jobs-16+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-16+-purple?style=for-the-badge" alt="Companies">
  <img src="https://img.shields.io/badge/updated-every%206h-green?style=for-the-badge" alt="Update Frequency">
  <img src="https://img.shields.io/github/license/digidai/openjobs?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/stars/digidai/openjobs?style=for-the-badge" alt="Stars">
</p>

<h1 align="center">OpenJobs</h1>

<p align="center">
  <strong>A free, open-source job aggregator that automatically collects and displays job listings from top companies.</strong>
</p>

<p align="center">
  <a href="https://digidai.github.io/openjobs">GitHub Pages</a> ·
  <a href="https://openjobs.genedai.me">Cloudflare Mirror</a> ·
  <a href="#features">Features</a> ·
  <a href="#quick-start">Quick Start</a> ·
  <a href="#contributing">Contributing</a>
</p>

---

## Why OpenJobs?

Most job boards are cluttered with ads, require sign-ups, or hide the best listings behind paywalls. **OpenJobs** is different:

- **100% Free & Open Source** - No ads, no paywalls, no sign-ups
- **Auto-Updated Every 6 Hours** - Fresh jobs from 16+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Engineering | 4 |
| Other | 4 |
| Healthcare | 3 |
| Management | 3 |
| Finance | 2 |
| Sales | 0 |
| Marketing | 0 |
| HR | 0 |
| Operations | 0 |

**Top Hiring Companies:** Crash Champions, Michigan Medicine, JPMorganChase, Cowlitz Family Health Center, Idaho First Bank

## Features

| Feature | Description |
|---------|-------------|
| **Auto Discovery** | Automatically finds and fetches the latest job data sources |
| **Smart Parsing** | Multi-format job caption parser (9+ strategies) for better data extraction |
| **Image Optimization** | CDN-powered image optimization with WebP conversion and lazy loading |
| **Smart Rotation** | Jobs rotate every 6 hours to show fresh content |
| **Dual Deployment** | GitHub Pages (table view) + Cloudflare Pages (card view) |
| **Company Logos** | Visual company branding for easy recognition |
| **Mobile Responsive** | Works perfectly on all device sizes |
| **SEO Enhanced** | Schema.org structured data, breadcrumbs, FAQ, and meta tags |
| **Accessibility** | WCAG compliant with ARIA labels, skip links, and keyboard navigation |
| **Daily Sitemaps** | SEO-friendly XML sitemaps updated automatically |

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        GitHub Actions                           │
│                    (Scheduled every 6h)                         │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    update_readme.py                             │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────────────┐   │
│  │ Fetch XML   │ → │ Parse Jobs  │ → │ Generate Output     │   │
│  │ Sitemap     │   │ (16+ jobs) │   │ (README + HTML)     │   │
│  └─────────────┘   └─────────────┘   └─────────────────────┘   │
└─────────────────────────┬───────────────────────────────────────┘
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
┌─────────────────────┐       ┌─────────────────────┐
│   GitHub Pages      │       │  Cloudflare Pages   │
│   (README.md)       │       │  (public/index.html)│
│   Table Layout      │       │   Card Grid Layout  │
│   200 jobs/page     │       │   50 jobs/page      │
└─────────────────────┘       └─────────────────────┘
```

## Quick Start

### Prerequisites

- Python 3.11+
- Git

### Local Development

```bash
# Clone the repository
git clone https://github.com/digidai/openjobs.git
cd openjobs

# Run the update script
python scripts/update_readme.py

# View the generated files
open README.md           # GitHub Pages content
open public/index.html   # Cloudflare Pages content
```

### Deploy Your Own

1. **Fork this repository**

2. **Enable GitHub Pages**
   - Go to Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main` / `root`

3. **Enable GitHub Actions**
   - Go to Actions tab
   - Enable workflows
   - Jobs will auto-update every 6 hours

4. **(Optional) Deploy to Cloudflare Pages**
   - Connect your forked repo
   - Build command: (none)
   - Output directory: `public`

## Configuration

Edit `scripts/update_readme.py` to customize:

| Variable | Default | Description |
|----------|---------|-------------|
| `JOBS_PER_PAGE` | 200 | Number of jobs shown on README |
| `HTML_JOBS_COUNT` | 50 | Number of jobs in HTML page |
| `ROTATION_HOURS` | 6 | Hours between job rotation |
| `CF_SITE_URL` | `https://openjobs.genedai.me` | Cloudflare Pages URL |
| `GH_SITE_URL` | `https://digidai.github.io/openjobs` | GitHub Pages URL |
| `IMAGE_CDN_ENABLED` | `True` | Enable/disable CDN image optimization |
| `IMAGE_CDN_URL` | `https://images.weserv.nl/?url=` | CDN service URL |
| `IMAGE_QUALITY` | 80 | Image quality (1-100) |
| `LOGO_WIDTH/HEIGHT` | 24 | Logo dimensions in pixels |

## Data Source

Jobs are aggregated from [OpenJobs AI](https://www.openjobs-ai.com), which collects listings from:

- **Tech**: Google, Amazon, Microsoft, Salesforce, SpaceX, and more
- **Healthcare**: Mayo Clinic, CVS Health, Northwell Health, and more
- **Finance**: CME Group, Fidelity, First Citizens Bank, and more
- **Retail**: Macy's, CVS, and more
- **And 16+ other companies**

## Project Structure

```
openjobs/
├── .github/
│   ├── workflows/          # GitHub Actions automation
│   └── ISSUE_TEMPLATE/     # Issue templates
├── scripts/
│   └── update_readme.py    # Main Python script
├── public/
│   ├── index.html          # Cloudflare Pages site
│   ├── stats.json          # Job statistics API
│   └── sitemap.xml         # Cloudflare sitemap
├── README.md               # This file (also GitHub Pages)
├── sitemap.xml             # GitHub Pages sitemap
├── _config.yml             # Jekyll configuration
├── LICENSE                 # MIT License
└── CONTRIBUTING.md         # Contribution guidelines
```

## Recent Enhancements

### 🚀 Performance & Quality Improvements (v2.0)

**Data Parsing (14.7x better location extraction)**
- Implemented 9-format job caption parser supporting:
  - `Title at Company in Location`
  - `Title at Company - Location`
  - `Title at Company | Location`
  - `Title - Company - Location`
  - `Title @ Company (Location)`
  - And more fallback strategies
- Location coverage improved from 0.4% to 6.28%

**Image Optimization**
- Free CDN integration (images.weserv.nl)
- Automatic WebP conversion with fallback
- Optimized dimensions (24x24px logos)
- Quality compression (80%)
- DNS prefetch and preconnection
- Lazy loading for better performance

**SEO Enhancements**
- Schema.org structured data:
  - BreadcrumbList for navigation
  - FAQPage for common questions
  - ItemList for job postings
  - Organization and WebSite schemas
- Enhanced meta tags (application-name, theme-color)
- Mobile web app capable

**Accessibility (WCAG Compliant)**
- Skip to main content link
- Comprehensive ARIA labels
- Keyboard navigation support
- Screen reader friendly
- Focus management

**Code Quality**
- Zero pyflakes warnings
- Enhanced error handling
- Detailed parse statistics
- Better logging and monitoring

## Roadmap

- [ ] Job search/filter functionality
- [ ] Job category tags
- [ ] Salary information (when available)
- [ ] Remote job filtering
- [ ] Email notifications for new jobs
- [ ] RSS feed support
- [x] Job statistics dashboard

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting a PR.

### Ways to Contribute

- Report bugs or suggest features via [Issues](https://github.com/digidai/openjobs/issues)
- Improve documentation
- Add new features
- Optimize performance

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Job data provided by [OpenJobs AI](https://www.openjobs-ai.com)
- Hosted on [GitHub Pages](https://pages.github.com) and [Cloudflare Pages](https://pages.cloudflare.com)

---

<h2 align="center">Latest Job Openings</h2>

<p align="center">
  <em>Updated January 31, 2026 · Showing 16 of 16+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Slalom Flex (Project Based) – Technical Engineer (Pega) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/c7/354aadd3c672fa95db63164a005c4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Slalom | [View](https://www.openjobs-ai.com/jobs/slalom-flex-project-based-technical-engineer-pega-charlotte-nc-130208870957056002) |
| Lead Mental Health Technician - FT Evenings | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/a7/c28b47b6e94b9817a5110623ee6e5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Valle Vista Health System | [View](https://www.openjobs-ai.com/jobs/lead-mental-health-technician-ft-evenings-greenwood-in-130208870957056003) |
| Lab Aide, Nights | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/bd/b4672e469e4db56887581519a441a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Flowers Hospital | [View](https://www.openjobs-ai.com/jobs/lab-aide-nights-dothan-al-130208954843136000) |
| Director, Planning & Design | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/20/39483a833a7b4a863871884486c66.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Gideons International | [View](https://www.openjobs-ai.com/jobs/director-planning-design-nashville-tn-130208954843136001) |
| Principal Solution Architect | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/44/653a024bda5fe1ace260bad67aff9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> TiDB, powered by PingCAP | [View](https://www.openjobs-ai.com/jobs/principal-solution-architect-united-states-130208954843136002) |
| MEAT/ASST DEPT LEADER | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/meatasst-dept-leader-st-matthews-ky-130208954843136003) |
| Senior Machinist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e0/c8fee693d9bb359e6bf930e8bce47.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> B&H Tool Company | [View](https://www.openjobs-ai.com/jobs/senior-machinist-san-marcos-ca-130209034534912000) |
| Staff Infrastructure Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/79/63364489cc8fbeb2c6a96d2974200.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> TwelveLabs | [View](https://www.openjobs-ai.com/jobs/staff-infrastructure-engineer-united-states-130209231667200000) |
| Collision Estimator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/fd/86d398e2d5a90df1bbd83a125db6f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Crash Champions | [View](https://www.openjobs-ai.com/jobs/collision-estimator-san-leandro-ca-130208728350720004) |
| Respiratory Therapist Intermediate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/65/0dcec15e5638733ac5026977fb15f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Michigan Medicine | [View](https://www.openjobs-ai.com/jobs/respiratory-therapist-intermediate-ann-arbor-mi-130208728350720005) |
| Part Time (30 Hours) Associate Banker, Foothill Blvd Branch, Hayward, CA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/80/20f3cd27af58eca9c48426bfb1c4f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> JPMorganChase | [View](https://www.openjobs-ai.com/jobs/part-time-30-hours-associate-banker-foothill-blvd-branch-hayward-ca-hayward-ca-130208728350720006) |
| Dental Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/34/1d554a390a9922ba0049659aa24b2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cowlitz Family Health Center | [View](https://www.openjobs-ai.com/jobs/dental-assistant-woodland-wa-130208728350720007) |
| Personal Banker I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/d9/03d0c126c4eab5426b602d513dc2f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Idaho First Bank | [View](https://www.openjobs-ai.com/jobs/personal-banker-i-bend-or-130208728350720008) |
| Engineering Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/aa/b446a056cb936310ce29b0471efbe.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SAIC | [View](https://www.openjobs-ai.com/jobs/engineering-technician-middletown-ri-130208728350720009) |
| Exchanger | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/0e/08b1c8f53dfe659363854cd39eb3e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BMTRUST | [View](https://www.openjobs-ai.com/jobs/exchanger-united-states-130208870957056000) |
| Senior Bid Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/e4/73ed366937e9b98d7c1d6f81103d6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NTT Global Data Centers | [View](https://www.openjobs-ai.com/jobs/senior-bid-manager-united-states-130208870957056001) |

<p align="center">
  <em>...and 0 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated January 31, 2026
</p>
