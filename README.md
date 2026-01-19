<p align="center">
  <img src="https://img.shields.io/badge/jobs-25+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-24+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 24+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 9 |
| Healthcare | 6 |
| Management | 4 |
| Sales | 2 |
| Operations | 2 |
| Engineering | 1 |
| Finance | 1 |
| Marketing | 0 |
| HR | 0 |

**Top Hiring Companies:** AdventHealth, CVS Health, Varda Space Industries, Project Brains, State of South Carolina

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
│  │ Sitemap     │   │ (25+ jobs) │   │ (README + HTML)     │   │
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
- **And 24+ other companies**

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
  <em>Updated January 19, 2026 · Showing 25 of 25+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Nurse Practitioner - NP/PA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/nurse-practitioner-nppa-charlotte-nc-125858052308992036) |
| Lead, Sales Operations | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/a4/123f408a7ac357c70fa739428994e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varda Space Industries | [View](https://www.openjobs-ai.com/jobs/lead-sales-operations-washington-dc-125858052308992037) |
| Trading program manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/9f/c3827ee19c2775e46957c023086bc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Project Brains | [View](https://www.openjobs-ai.com/jobs/trading-program-manager-houston-county-tx-125858232664064000) |
| Sign Language Interpreter (ADJT25) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/bc/2f275e81504887c7d01c05bcd8c14.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> State of South Carolina | [View](https://www.openjobs-ai.com/jobs/sign-language-interpreter-adjt25-aiken-county-sc-125858232664064001) |
| Director of Accounting- Revenue Assurance | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/be/b85465d407e9c4a2eb7c1a6881c55.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Aspen Skiing Company | [View](https://www.openjobs-ai.com/jobs/director-of-accounting-revenue-assurance-denver-co-125858232664064002) |
| Staff MFG Process Engineer (Process Owner) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/2e/1862abc36af462a187ea3d32aa143.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ZT Systems | [View](https://www.openjobs-ai.com/jobs/staff-mfg-process-engineer-process-owner-secaucus-nj-125858232664064003) |
| Registered Nurse CVOR | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/08/9a72c48bbf0ef2890317158be3530.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AdventHealth | [View](https://www.openjobs-ai.com/jobs/registered-nurse-cvor-daytona-beach-fl-125858232664064004) |
| Project Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/c9/a15d57653dcceecc15bd4d46dea22.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Steven Douglas Corp. | [View](https://www.openjobs-ai.com/jobs/project-manager-concord-oh-125858232664064005) |
| Radiology Technologist Part Time Nights | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/08/9a72c48bbf0ef2890317158be3530.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AdventHealth | [View](https://www.openjobs-ai.com/jobs/radiology-technologist-part-time-nights-killeen-tx-125858232664064006) |
| Assistant Branch Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/d6/a5e3165965aaedb822c5daec542e5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Wellby Financial | [View](https://www.openjobs-ai.com/jobs/assistant-branch-manager-friendswood-tx-125858232664064007) |
| Clinical Psychologist (PhD or Psy D) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/01/8fce3b4f122795f1a71673fa2dcf3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> LifeStance Health | [View](https://www.openjobs-ai.com/jobs/clinical-psychologist-phd-or-psy-d-concord-nh-125858232664064008) |
| Ground Torch Cutter Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/cf/d21090c8fc3663ff83796568ab899.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SA Recycling | [View](https://www.openjobs-ai.com/jobs/ground-torch-cutter-supervisor-brownsville-tx-125858232664064009) |
| Registered Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/99/28a94e9f039e27625224a4c0ddb9b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Laurel Ridge Treatment Center | [View](https://www.openjobs-ai.com/jobs/registered-nurse-san-antonio-texas-metropolitan-area-125858232664064010) |
| Electrical Technician I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/42/677cd0b739eb86d68e097518bf172.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SJE Inc. | [View](https://www.openjobs-ai.com/jobs/electrical-technician-i-birmingham-al-125858232664064011) |
| Warehouse Associate II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/ea/ec9ce3246f49f8de0498775685730.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Schneider Electric | [View](https://www.openjobs-ai.com/jobs/warehouse-associate-ii-seneca-sc-125858232664064012) |
| Machine Operator - 2nd Shift w/10% Diff 03:00p-11:15p Mon-Fri | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/a1/a3b88172f68b1327138b9be5347a8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Flex | [View](https://www.openjobs-ai.com/jobs/machine-operator-2nd-shift-w10-diff-0300p-1115p-mon-fri-austin-tx-125858480128000000) |
| Home Care Occupational Therapist- Per Diem | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/e6/7f2f0abcea43f1d70bf35bff91ea3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Metro Physical & Aquatic Therapy | [View](https://www.openjobs-ai.com/jobs/home-care-occupational-therapist-per-diem-deer-park-ny-125858480128000001) |
| Logistics & Process Training Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/e4/38bd6ddb3c193c865ff7ad390da98.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Carvana | [View](https://www.openjobs-ai.com/jobs/logistics-process-training-specialist-tempe-az-125858480128000002) |
| Vice President of Business Development | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/20/b2505bee1f586504611d0bf0db4b8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lisinski Law Firm | [View](https://www.openjobs-ai.com/jobs/vice-president-of-business-development-riverside-ca-125858480128000003) |
| Business Office Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/40/9e145f2f3fc10e66215c9f6e06b1d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lexington Medical Center | [View](https://www.openjobs-ai.com/jobs/business-office-associate-west-columbia-sc-125858480128000004) |
| Fraud Investigator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/21/9be8994730c07d8d6cafdbe9b6468.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ADP | [View](https://www.openjobs-ai.com/jobs/fraud-investigator-san-dimas-ca-125858480128000005) |
| Entry Level Hospital Services Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/97/0304cb56552a3725bbd8f908427ed.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Stericycle | [View](https://www.openjobs-ai.com/jobs/entry-level-hospital-services-technician-fort-myers-fl-125858480128000006) |
| Neurology Physician Assistant Per Diem | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/43/22ecadc07886b17b3ef5fad15e04b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Northwell Health | [View](https://www.openjobs-ai.com/jobs/neurology-physician-assistant-per-diem-staten-island-ny-125858660483072000) |
| Right-of-Way Agent | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/df/cb7cf2be79c98ef01d478f5ed1ead.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CW Solutions, Inc. d/b/a CW Solutions | [View](https://www.openjobs-ai.com/jobs/right-of-way-agent-new-brunswick-nj-125858740174848000) |
| Bus Driver | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/c8/5f401f04d116330660c7ecaa852ed.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Showering Love | [View](https://www.openjobs-ai.com/jobs/bus-driver-davie-fl-125858916335616000) |

<p align="center">
  <em>...and 0 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated January 19, 2026
</p>
