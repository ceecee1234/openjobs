<p align="center">
  <img src="https://img.shields.io/badge/jobs-17+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-17+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 17+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Healthcare | 7 |
| Engineering | 5 |
| Other | 5 |
| Sales | 0 |
| Finance | 0 |
| Management | 0 |
| Marketing | 0 |
| HR | 0 |
| Operations | 0 |

**Top Hiring Companies:** Trinity Health, United Surgical Partners International, Inc, Apple, Global Life Science Hub, BAYADA Home Health Care

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
│  │ Sitemap     │   │ (17+ jobs) │   │ (README + HTML)     │   │
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
- **And 17+ other companies**

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
  <em>Updated January 27, 2026 · Showing 17 of 17+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Senior Principal Platform Architect - Financial Markets and Insurance | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/1c/d6e549ab60b728497f73aeeccc9ba.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ServiceNow | [View](https://www.openjobs-ai.com/jobs/senior-principal-platform-architect-financial-markets-and-insurance-denver-co-128758400942080001) |
| Laboratory Assistant Phlebotomist (ANMC Laboratory) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/d0/f2d090d0e36f8a728ea7af072ac3e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Alaska Native Tribal Health Consortium (ANTHC) | [View](https://www.openjobs-ai.com/jobs/laboratory-assistant-phlebotomist-anmc-laboratory-anchorage-ak-128758509993984000) |
| Family Law Attorney (Relocation Required, Assistance Provided) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/43/3a022692132c21baf700c0f2f4fce.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Virga Law Firm, P.A. | [View](https://www.openjobs-ai.com/jobs/family-law-attorney-relocation-required-assistance-provided-alabama-united-states-128758644211712000) |
| MOVER INSTALLATION TECHNICIAN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/a1/8502fa8686f2aa1b6d9a8ce5ac682.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Moffitt Cancer Center | [View](https://www.openjobs-ai.com/jobs/mover-installation-technician-tampa-fl-128758644211712001) |
| Registered Nurse - Emergency Department Weekends | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/fd/87e099ca4630b42393bb3f9f936c9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Trinity Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-emergency-department-weekends-mishawaka-in-128758191226880000) |
| Clinical RN Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/cf/cdbfd20f03eb342877ff91b76567e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> United Surgical Partners International, Inc | [View](https://www.openjobs-ai.com/jobs/clinical-rn-director-colorado-springs-co-128758191226880001) |
| GNSS Hardware Systems Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/f3/870be274f6c49b3e31a0c6728957f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Apple | [View](https://www.openjobs-ai.com/jobs/gnss-hardware-systems-engineer-san-diego-ca-128758191226880002) |
| Manufacturing Associate (USP or DSP) - Relocation Available | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/65/fb204b39c91d2170c81fe872443ff.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Global Life Science Hub | [View](https://www.openjobs-ai.com/jobs/manufacturing-associate-usp-or-dsp-relocation-available-new-jersey-united-states-128758191226880003) |
| Registered Nurse, Home Health Visits | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/25/fdf5c5d48111aedbf1d70ee1845f9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BAYADA Home Health Care | [View](https://www.openjobs-ai.com/jobs/registered-nurse-home-health-visits-york-pa-128758191226880004) |
| Account Manager Pharmacy | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/b3/1da1985ce05807ec319a8c136023e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Guardian Pharmacy | [View](https://www.openjobs-ai.com/jobs/account-manager-pharmacy-randolph-nj-128758191226880005) |
| Customer Service Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/30/b06b9907198d68f229aeb3e8430cf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Insight Global | [View](https://www.openjobs-ai.com/jobs/customer-service-representative-phoenix-az-128758191226880006) |
| Risk Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/7b/a6621c260b225e06301b9b73047f6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Loss Control | [View](https://www.openjobs-ai.com/jobs/risk-engineer-loss-control-remote-morristown-nj-128758191226880007) |
| Manufacturing Engineering Intern- Ludington, MI | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/5f/de8a4cee1160b216a52fe9f55ee75.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Haworth | [View](https://www.openjobs-ai.com/jobs/manufacturing-engineering-intern-ludington-mi-ludington-mi-128758191226880008) |
| Operations Program Management Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/08/6b7607a2ddd33510caa482ce438e6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Zoox | [View](https://www.openjobs-ai.com/jobs/operations-program-management-intern-foster-city-ca-128758325444608000) |
| Phlebotomist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/2e/41fce0e9b1376cd760e7c7b862b50.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mission Health | [View](https://www.openjobs-ai.com/jobs/phlebotomist-asheville-nc-128758325444608001) |
| RN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/9d/773d97aa4d8cf51016d8da1253ecf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ET3 Tele | [View](https://www.openjobs-ai.com/jobs/rn-et3-tele-fountain-valley-ft-nights-fountain-valley-ca-128758325444608002) |
| Software Engineering Technical Leader - Silicon One Customer Engineering | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/fe/af10390e560aea745ccba53e044ed.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cisco | [View](https://www.openjobs-ai.com/jobs/software-engineering-technical-leader-silicon-one-customer-engineering-san-jose-ca-128758400942080000) |

<p align="center">
  <em>...and 0 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated January 27, 2026
</p>
