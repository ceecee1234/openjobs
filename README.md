<p align="center">
  <img src="https://img.shields.io/badge/jobs-979+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-714+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 714+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 402 |
| Healthcare | 208 |
| Management | 161 |
| Engineering | 123 |
| Sales | 51 |
| Finance | 15 |
| Operations | 10 |
| HR | 6 |
| Marketing | 3 |

**Top Hiring Companies:** Lensa, Shift, DataAnnotation, CVS Health, PwC

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
│  │ Sitemap     │   │ (979+ jobs) │   │ (README + HTML)     │   │
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
- **And 714+ other companies**

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
  <em>Updated January 27, 2026 · Showing 200 of 979+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| CNA - Pre-Op/PACU | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/92/d62a77d2e54dd31442ff41c1de685.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Gibson Area Hospital & Health Services | [View](https://www.openjobs-ai.com/jobs/cna-pre-oppacu-gibson-city-il-128391932018688752) |
| Park Maintenance Supervisor (November 2025) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/2c/ae38935c92c19df83981e986c10a7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> City of Richmond Heights, Missouri | [View](https://www.openjobs-ai.com/jobs/park-maintenance-supervisor-november-2025-richmond-heights-mo-128391932018688753) |
| Sales & Marketing Internship | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/47/114ed2bfa29c42510008b7733248b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Shift | [View](https://www.openjobs-ai.com/jobs/sales-marketing-internship-baton-rouge-la-128391932018688754) |
| Technical Test Lead | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/61/6827db04debdb52286b1b5c31439d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Infosys | [View](https://www.openjobs-ai.com/jobs/technical-test-lead-morrisville-nc-128391932018688755) |
| Math Curriculum Specialist- Southeast Michigan | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/98/f924168dc9c6303e0fc533cc6901b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> National Heritage Academies | [View](https://www.openjobs-ai.com/jobs/math-curriculum-specialist-southeast-michigan-canton-mi-128391932018688756) |
| Pharmacy Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/pharmacy-intern-solana-beach-ca-128391932018688757) |
| Senior Interior Designer - 2V6S002 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/6c/cb86a50602662b962deeeca2fc2bd.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SNIPEBRIDGE | [View](https://www.openjobs-ai.com/jobs/senior-interior-designer-2v6s002-west-palm-beach-fl-128391932018688758) |
| Structural Mechanic V - Special Missions | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/8b/2d6e61af8c570029400fbbca59b87.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Gulfstream Aerospace | [View](https://www.openjobs-ai.com/jobs/structural-mechanic-v-special-missions-savannah-ga-128391932018688759) |
| Insurance Agent (Base salary + Uncapped commissions) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/1b/ab5fc6d964f0230a404742fb81611.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Comparion Insurance Agency | [View](https://www.openjobs-ai.com/jobs/insurance-agent-base-salary-uncapped-commissions-gainesville-ga-128391932018688760) |
| Tactile ASL (American Sign Language) Interpreter | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/55/a419eb4eabe3e97b4797beda34142.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hanna Interpreting Services LLC | [View](https://www.openjobs-ai.com/jobs/tactile-asl-american-sign-language-interpreter-oakland-ca-128391932018688761) |
| DSP Lead Float | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/5e/6b2c3b865437f0974e9672d229667.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lutheran Social Service of Minnesota | [View](https://www.openjobs-ai.com/jobs/dsp-lead-float-bemidji-mn-128391932018688762) |
| PLM, Accessories - Bags & Socks | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/f3/5e5032ad69050d93278fcd742b61e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Under Armour | [View](https://www.openjobs-ai.com/jobs/plm-accessories-bags-socks-baltimore-md-128391932018688763) |
| Vehicle Mechanic | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/b8/8662840107951584e5dc762f3d8ab.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jet Aviation | [View](https://www.openjobs-ai.com/jobs/vehicle-mechanic-teterboro-nj-128391932018688764) |
| Pharmacy Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/pharmacy-intern-honolulu-hi-128391932018688765) |
| Dietitian – Inpatient | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/32/3df8af0778ebe97703e9426347c8c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mayo Clinic | [View](https://www.openjobs-ai.com/jobs/dietitian-inpatient-la-crosse-wi-128391932018688766) |
| Outsourced Accounting Controller - Technology Industry Clients | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/b6/7761e9ed629755fdad6fc912c9597.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Wipfli | [View](https://www.openjobs-ai.com/jobs/outsourced-accounting-controller-technology-industry-clients-southfield-mi-128391932018688767) |
| CT Technologist FSED | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/57/4f967fed7044c6047aec3fffc94ae.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HCA Florida Twin Cities Hospital | [View](https://www.openjobs-ai.com/jobs/ct-technologist-fsed-niceville-fl-128391932018688768) |
| LPN Rehab | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/b7/6d6f721e98b27d98068c0a21c801b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Wesley Healthcare | [View](https://www.openjobs-ai.com/jobs/lpn-rehab-wichita-ks-128391932018688769) |
| Corporate Finance Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/96/0eb3c674ecd318cdf587805092de3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Life360 | [View](https://www.openjobs-ai.com/jobs/corporate-finance-manager-united-states-128391932018688770) |
| Physical Therapist Home Health | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/be/e2db445ab9caf54973d2c3d730de2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CenterWell Home Health | [View](https://www.openjobs-ai.com/jobs/physical-therapist-home-health-ontario-ca-128391932018688771) |
| Entry Level Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/50/b9290a5d6a0f69a7444312cfe9ede.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Thomas KIA of Highland | [View](https://www.openjobs-ai.com/jobs/entry-level-technician-highland-in-128391932018688772) |
| Warehouse Sorter | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/2d/ab95a31ca9b6f42de1d6cfc26348b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NOW Courier Inc. | [View](https://www.openjobs-ai.com/jobs/warehouse-sorter-indianapolis-in-128391932018688773) |
| Compliance | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/80/20f3cd27af58eca9c48426bfb1c4f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> United States | [View](https://www.openjobs-ai.com/jobs/compliance-united-states-2026-reentry-program-plano-tx-128391932018688774) |
| Pharmacy Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/pharmacy-intern-lebanon-tn-128391932018688775) |
| Associate Paralegal, Privacy | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/f6/adfa31c5a3a3f0026c37cff970bfc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> GitLab | [View](https://www.openjobs-ai.com/jobs/associate-paralegal-privacy-united-states-128391932018688776) |
| Sr Nuclear Quality Assurance Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/53/469cabddaea29bd5feb81e6b820e0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SHINE Technologies | [View](https://www.openjobs-ai.com/jobs/sr-nuclear-quality-assurance-engineer-janesville-wi-128391932018688777) |
| Operations Administrator / IPM / Northwest Physicians Group | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/74/d4ca46a65718c5f9c22b621b32a31.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Northwest Texas Healthcare System | [View](https://www.openjobs-ai.com/jobs/operations-administrator-ipm-northwest-physicians-group-amarillo-tx-128391932018688778) |
| CLINICAL THERAPIST | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/01/0d2344dfb5af6ce142a2ede4626cf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CERTUS Psychiatry and Integrated Care | [View](https://www.openjobs-ai.com/jobs/clinical-therapist-clemmons-nc-128391932018688779) |
| Insurance Agent (Base salary + Uncapped commissions) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/1b/ab5fc6d964f0230a404742fb81611.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Comparion Insurance Agency | [View](https://www.openjobs-ai.com/jobs/insurance-agent-base-salary-uncapped-commissions-suwanee-ga-128391932018688780) |
| Logistics Associate I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/39/7ced38162a5c7b7b3d33004e9a0d2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Yale New Haven Health | [View](https://www.openjobs-ai.com/jobs/logistics-associate-i-new-haven-ct-128391932018688781) |
| Senior Director of Product | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/b6/b4c8777e5e66b7b780f78101a4afc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Toptal | [View](https://www.openjobs-ai.com/jobs/senior-director-of-product-united-states-128391932018688782) |
| Manager, Market Development - Engineered Wood Products | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/58/6bb4de96894fbeb6cf81e2173c9e1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Canfor | [View](https://www.openjobs-ai.com/jobs/manager-market-development-engineered-wood-products-el-dorado-ar-128391932018688783) |
| Nocturnist Mid-Shift APP | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/7c/634e95602266c396b589fec270d33.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hospitalist | [View](https://www.openjobs-ai.com/jobs/nocturnist-mid-shift-app-hospitalist-audubon-louisville-ky-128391932018688785) |
| Process Planner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/09/89eb2120d49932498958e3cba5491.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HOLON | [View](https://www.openjobs-ai.com/jobs/process-planner-jacksonville-fl-128391932018688786) |
| Banking Associate - Great Barrington | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/26/726e60bd1215f36719a308a25b798.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> TD | [View](https://www.openjobs-ai.com/jobs/banking-associate-great-barrington-great-barrington-ma-128391932018688787) |
| Speech Language Pathologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/9b/6727c35f582b0b3c35464a8c92a18.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Reliant Rehabilitation | [View](https://www.openjobs-ai.com/jobs/speech-language-pathologist-enumclaw-wa-128391932018688788) |
| Senior Engineer - Advanced Test Software | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/8d/e76be154592094de23849bed78daa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BAE Systems, Inc. | [View](https://www.openjobs-ai.com/jobs/senior-engineer-advanced-test-software-westminster-co-128391932018688789) |
| FP&A Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/ce/4ab96c901bc5d36d37462ac1130a1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Fabric | [View](https://www.openjobs-ai.com/jobs/fpa-manager-new-york-ny-128391932018688790) |
| PRODUCE/ASST DEPT LEADER | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/c42add1f96f9e2717cfc8ce23c30d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kroger Mountain View Foods | [View](https://www.openjobs-ai.com/jobs/produceasst-dept-leader-stevens-point-wi-128391932018688791) |
| Pharmacy Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/pharmacy-intern-oceanside-ca-128391932018688792) |
| Executive Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/75/979265ae7f941422bfb03aab8c032.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Oaks Senior Living | [View](https://www.openjobs-ai.com/jobs/executive-director-georgia-united-states-128391932018688793) |
| Senior IT Auditor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/31/c355f962264017ad17757c782dcf7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Northwest Bank | [View](https://www.openjobs-ai.com/jobs/senior-it-auditor-columbus-oh-128391932018688794) |
| Pharmacy Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/pharmacy-intern-atwater-ca-128391932018688795) |
| VP – Wealth Services, Alternatives & Private Markets Solutions Product Execution | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/82/2c7d6c9873a42a97f1800184abb75.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BNY | [View](https://www.openjobs-ai.com/jobs/vp-wealth-services-alternatives-private-markets-solutions-product-execution-new-york-ny-128391932018688796) |
| Patient Logistics Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/31/ad544086ab956438affa3814a8fa7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HCA Healthcare | [View](https://www.openjobs-ai.com/jobs/patient-logistics-specialist-plano-tx-128391932018688797) |
| Nurse Aide Certified (GP 8) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/32/cb5852d3bffb2d42f86e562bbdc5e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Appalachian Regional Healthcare (ARH) | [View](https://www.openjobs-ai.com/jobs/nurse-aide-certified-gp-8-whitesburg-ky-128391932018688798) |
| Software Platform Engineering Manager - Ubuntu for Next-Gen Silicon | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/7f/288c3a0010721cfb7ac0f4d0fec27.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Canonical | [View](https://www.openjobs-ai.com/jobs/software-platform-engineering-manager-ubuntu-for-next-gen-silicon-san-jose-ca-128391932018688801) |
| Manager, Strategic Enterprise Sales | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/84/b2d05914b2749622963c1ef058ed5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Rippling | [View](https://www.openjobs-ai.com/jobs/manager-strategic-enterprise-sales-austin-tx-128391932018688802) |
| Security Rep | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/00/9441f427f26d04f8d6583d2ec74ea.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lockheed Martin | [View](https://www.openjobs-ai.com/jobs/security-rep-honolulu-hi-128391932018688803) |
| Senior Scientific Director, PTCE | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/a9/a138705e757ac6f716b10b399295a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MJH Life Sciences® | [View](https://www.openjobs-ai.com/jobs/senior-scientific-director-ptce-united-states-128391932018688804) |
| Physical Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/09/9c4fdc666c6fb7f228bbcdf9dfbbc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> University of Utah Health | [View](https://www.openjobs-ai.com/jobs/physical-therapist-salt-lake-city-ut-128391932018688805) |
| Finance Intern (Summer 2026) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/26/e35250cd6d2cfb6ada09e62b3ba69.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Dyno Nobel | [View](https://www.openjobs-ai.com/jobs/finance-intern-summer-2026-salt-lake-city-ut-128391932018688806) |
| Tax Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/9f/00e89f40ca08dc315693847baf03b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> firstPRO, Inc | [View](https://www.openjobs-ai.com/jobs/tax-manager-philadelphia-pa-128391932018688808) |
| Physical Therapist - Greater Chatham, NJ | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/48/ee787deb461ba844ccaa6e7c7c5a2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> FOX Rehabilitation | [View](https://www.openjobs-ai.com/jobs/physical-therapist-greater-chatham-nj-chatham-nj-128391932018688809) |
| Senior Consultant - Private Equity Advisory | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/d3/7714ed222fa24fbe6f858d50944db.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CrossCountry Consulting | [View](https://www.openjobs-ai.com/jobs/senior-consultant-private-equity-advisory-united-states-128391932018688810) |
| Sales & Business Internship | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/47/114ed2bfa29c42510008b7733248b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Shift | [View](https://www.openjobs-ai.com/jobs/sales-business-internship-minot-nd-128391932018688811) |
| Tax Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/37/7c5fc768db8e0accb17c715b8a562.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> EisnerAmper | [View](https://www.openjobs-ai.com/jobs/tax-director-boston-ma-128391932018688812) |
| CNC Machinist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/8b/6a24068267aa9c75b996af98e28e0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> 2nd Shift | [View](https://www.openjobs-ai.com/jobs/cnc-machinist-2nd-shift-4-day-work-week-west-chesterfield-nh-128391932018688814) |
| Senior Director FP&A Deals Desk (NAM) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/de/1e9db895404e144f03055b11368d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Palo Alto Networks | [View](https://www.openjobs-ai.com/jobs/senior-director-fpa-deals-desk-nam-santa-clara-ca-128391932018688815) |
| Environmental Health & Safety Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/5c/fd90ee8a24e9b093f9899b6d65285.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Jackson Laboratory | [View](https://www.openjobs-ai.com/jobs/environmental-health-safety-manager-ellsworth-me-128391932018688816) |
| Zone Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/ea/b47751b78e880f8a7734b164eb51e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Compass Connections | [View](https://www.openjobs-ai.com/jobs/zone-supervisor-baytown-tx-128391932018688817) |
| Home Health Aide | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/be/e2db445ab9caf54973d2c3d730de2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CenterWell Home Health | [View](https://www.openjobs-ai.com/jobs/home-health-aide-omaha-ne-128391932018688818) |
| District Support Pharmacist PT | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/district-support-pharmacist-pt-lake-charles-la-128391932018688819) |
| VMDR Expert (Vulnerability Management, Detection & Response) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/79/64fa32bbcd2834a66dce317fb0955.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Armis | [View](https://www.openjobs-ai.com/jobs/vmdr-expert-vulnerability-management-detection-response-arlington-va-128391932018688820) |
| Arm & Hammer Animal Nutrition Dairy Business Development Manager (PA or NY) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/dd/4407494d01541ce53d4cdf1908927.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Church & Dwight Co., Inc. | [View](https://www.openjobs-ai.com/jobs/arm-hammer-animal-nutrition-dairy-business-development-manager-pa-or-ny-united-states-128391932018688821) |
| Manager FP&A, NA Plasma | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/de/a0bf702200e2e35832a5463dbedb9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Haemonetics | [View](https://www.openjobs-ai.com/jobs/manager-fpa-na-plasma-chittenden-county-vt-128391932018688822) |
| Systems Engineer, Mid- Level (8612) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/a5/b39ab3fe8aca4b636f255d0e88a2c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Patricio Enterprises, Inc. | [View](https://www.openjobs-ai.com/jobs/systems-engineer-mid-level-8612-stafford-va-128391932018688823) |
| RN-Manager Surgical Clinical Operations | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/6b/630918d54b43e14f4d506288fa81e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Eisenhower Health | [View](https://www.openjobs-ai.com/jobs/rn-manager-surgical-clinical-operations-rancho-mirage-ca-128391932018688824) |
| Occupational Therapy Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/9b/6727c35f582b0b3c35464a8c92a18.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Reliant Rehabilitation | [View](https://www.openjobs-ai.com/jobs/occupational-therapy-assistant-hot-springs-village-ar-128391932018688825) |
| Automotive Sales Consultant - Grand Rapids, Michigan, United States | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/cb/e557a1fe7a253f9efba5c149b06a1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> LaFontaine Automotive Group | [View](https://www.openjobs-ai.com/jobs/automotive-sales-consultant-grand-rapids-michigan-united-states-grand-rapids-mi-128391932018688826) |
| Specialist Senior/Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/39/954f26fc843dc265a62e9669e09d3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Deloitte | [View](https://www.openjobs-ai.com/jobs/specialist-seniorconsultant-st-louis-mo-128391932018688827) |
| Housing Navigator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/4b/1e315ab3e0b632b536f0e136bfba2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> U.S.VETS | [View](https://www.openjobs-ai.com/jobs/housing-navigator-inglewood-ca-128391932018688828) |
| Account Executive, Enterprise | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/8e/4053aeaf1f6d3f56db161be0af552.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hebbia | [View](https://www.openjobs-ai.com/jobs/account-executive-enterprise-new-york-ny-128391932018688829) |
| Technician - Process Quality Assurance Floor Support (Night Shift) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/fb/8466bd490fe0fbf86e4b2a0140416.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Eli Lilly and Company | [View](https://www.openjobs-ai.com/jobs/technician-process-quality-assurance-floor-support-night-shift-durham-nc-128391932018688831) |
| Director, Partner Engagement & Experience | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/c8/670b4731ae09bbdbf9d1d797730ac.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cohesity | [View](https://www.openjobs-ai.com/jobs/director-partner-engagement-experience-georgia-128391932018688832) |
| Local Delivery Driver (CDL A) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/ea/ab12bc0f8741865e133b2096706f9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Linde Gas & Equipment | [View](https://www.openjobs-ai.com/jobs/local-delivery-driver-cdl-a-salt-lake-city-ut-128391932018688833) |
| Project Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/19/bb4238c199c1a4d48a654ec50583c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Perkins&Will | [View](https://www.openjobs-ai.com/jobs/project-manager-dallas-tx-128391932018688834) |
| Radiologic Technologist (Rad Tech) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/74/5631928de1787fd8a34b114a62a3b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inova Fair Oaks Hospital | [View](https://www.openjobs-ai.com/jobs/radiologic-technologist-rad-tech-fairfax-va-128391932018688835) |
| Direct Sales Manager - Overland Park, KS (Kansas City Metro) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/ca/0a704965f1181e3e8fc747b2548a5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Steadily Insurance Company | [View](https://www.openjobs-ai.com/jobs/direct-sales-manager-overland-park-ks-kansas-city-metro-overland-park-ks-128391932018688836) |
| Pharmacy Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/pharmacy-intern-grosse-pointe-mi-128391932018688837) |
| Software Engineer - Core Product | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fa/0936ef38f125339ee19191dcc1e9d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Baseten | [View](https://www.openjobs-ai.com/jobs/software-engineer-core-product-new-york-ny-128391932018688838) |
| KC-130J Quality Assurance Inspector | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/65/2aaa466f9de764c7ddbc207b66f27.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> KC-130J Program | [View](https://www.openjobs-ai.com/jobs/kc-130j-quality-assurance-inspector-kc-130j-program-kuwait-madison-ms-128391932018688839) |
| Senior Associate, Email Marketing Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/cc/301ef851478e50797fb5463cba612.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Abacus Group, LLC | [View](https://www.openjobs-ai.com/jobs/senior-associate-email-marketing-specialist-new-york-city-metropolitan-area-128391932018688840) |
| High School Special Education Level III Para Educator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/de/7715c2587aee942165cd7d23db670.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Maquoketa Community Schol District | [View](https://www.openjobs-ai.com/jobs/high-school-special-education-level-iii-para-educator-maquoketa-ia-128391932018688841) |
| RN, Skilled Nursing and Rehab Center (FT, Nights) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/64/b1e59d83e57c73b7268d6aeb44954.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Allied Services | [View](https://www.openjobs-ai.com/jobs/rn-skilled-nursing-and-rehab-center-ft-nights-scranton-pa-128391932018688842) |
| Benefits Operations Specialist, Medical Benefits | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/76/72aeab8a536d9539ba09c5def6415.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Justworks | [View](https://www.openjobs-ai.com/jobs/benefits-operations-specialist-medical-benefits-new-york-ny-128391932018688843) |
| Call Specialist/Receptionist - Rural | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/25/31c02d806be4bce891abbb03730f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Family Service Association of San Antonio, Inc. | [View](https://www.openjobs-ai.com/jobs/call-specialistreceptionist-rural-crystal-city-tx-128391932018688844) |
| Assistant/Associate/Professor of Pediatrics Neurology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/94/623ffa3bcd99eefe6c127074a0065.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UI Health | [View](https://www.openjobs-ai.com/jobs/assistantassociateprofessor-of-pediatrics-neurology-chicago-il-128391932018688845) |
| Behavioral Health Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/9e/72733d166b518723e1bf1218d6e35.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Children's Hospital Colorado | [View](https://www.openjobs-ai.com/jobs/behavioral-health-specialist-aurora-co-128391932018688846) |
| Manufacturing Group Leader | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/01/d6bc9c12d1688e92fcf939d8f0843.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Production | [View](https://www.openjobs-ai.com/jobs/manufacturing-group-leader-production-wentzville-wentzville-mo-128391932018688847) |
| Test Engineer Intern, ESS (Summer 2026) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/28/9a3d203348db9edbe2d8621d31f85.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Peak Energy | [View](https://www.openjobs-ai.com/jobs/test-engineer-intern-ess-summer-2026-burlingame-ca-128391932018688848) |
| Software Platform Engineering Manager - Ubuntu for Next-Gen Silicon | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/7f/288c3a0010721cfb7ac0f4d0fec27.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Canonical | [View](https://www.openjobs-ai.com/jobs/software-platform-engineering-manager-ubuntu-for-next-gen-silicon-honolulu-hi-128391932018688850) |
| Containerization & Virtualisation Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/7f/288c3a0010721cfb7ac0f4d0fec27.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Canonical | [View](https://www.openjobs-ai.com/jobs/containerization-virtualisation-engineer-raleigh-nc-128391932018688851) |
| Chaplain I - PRN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/a8/fb3ab37959f0901daeba3ad01a372.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Baylor Scott & White Health | [View](https://www.openjobs-ai.com/jobs/chaplain-i-prn-dallas-tx-128391932018688852) |
| Pharmacy Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/pharmacy-intern-morgantown-wv-128391932018688853) |
| Customer Service Representative - State Farm Agent Team Member | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/29/6642d139b1a83b74ad10b919847a7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> State Farm Agent | [View](https://www.openjobs-ai.com/jobs/customer-service-representative-state-farm-agent-team-member-omaha-ne-128391932018688854) |
| Sales Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/5d/65e2ab5581dbb79bd7b703740e45c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Gallagher | [View](https://www.openjobs-ai.com/jobs/sales-associate-humble-tx-128391932018688855) |
| Sales Clinical Account Executive (CAE) El Paso Texas | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/41/102adc5b887622b7b86906b643081.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ANI Pharmaceuticals, Inc. | [View](https://www.openjobs-ai.com/jobs/sales-clinical-account-executive-cae-el-paso-texas-princeton-nj-128391932018688856) |
| 2nd Shift Slitter Operator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/2d/7bbd90994cfb90cebb81b089bac03.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Wieland Group | [View](https://www.openjobs-ai.com/jobs/2nd-shift-slitter-operator-wheeling-il-128391932018688857) |
| Technical Services Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/b0/65ec2854fb4a37e6cea936931dac3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BIOTRONIK | [View](https://www.openjobs-ai.com/jobs/technical-services-engineer-lake-oswego-or-128391932018688858) |
| Commercial Title Officer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/09/224a8f44bfadb48043ec3ecfe9757.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Stewart Title | [View](https://www.openjobs-ai.com/jobs/commercial-title-officer-westport-ct-128391932018688859) |
| Strategic Account Executive – (AAG) East | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/ed/47ce350e73981a9a6c4a3d6887bce.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Saviynt | [View](https://www.openjobs-ai.com/jobs/strategic-account-executive-aag-east-vermont-united-states-128391932018688860) |
| Systems Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/e0/adf72be56c2ba87af6f6be7df5da4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Areté | [View](https://www.openjobs-ai.com/jobs/systems-engineer-tucson-az-128391932018688861) |
| Creative Project Manager - Mandarin Speaking | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/fc/0fb483634a6228b9de65e2ab82deb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pattern® | [View](https://www.openjobs-ai.com/jobs/creative-project-manager-mandarin-speaking-lehi-ut-128391932018688862) |
| Field Service Representative/Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/d8/3b0300da0a9c5fe97c5e037c713a6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Stiles Machinery | [View](https://www.openjobs-ai.com/jobs/field-service-representativetechnician-san-antonio-tx-128391932018688863) |
| Associate Director, Drug Product Manufacturing Science & Technology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/4b/a4b80b3c7c8a74242014202aa3ced.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Takeda | [View](https://www.openjobs-ai.com/jobs/associate-director-drug-product-manufacturing-science-technology-brooklyn-park-mn-128391932018688864) |
| Pharmacy Intern | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e1/f4357a9bf0f3643b7bb5652854889.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CVS Health | [View](https://www.openjobs-ai.com/jobs/pharmacy-intern-sterling-heights-mi-128391932018688865) |
| Quant Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/a9/9ca2905bb348eded1d36a12bc0ebf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Python/Rust | [View](https://www.openjobs-ai.com/jobs/quant-developer-pythonrust-options-market-maker-new-york-united-states-128391932018688866) |
| Content Marketing Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/17/c527f15d2adb089b77f0b11a63b7c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mimica | [View](https://www.openjobs-ai.com/jobs/content-marketing-manager-united-states-128391932018688867) |
| Social Worker | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/e1/56e9f587a1ab4dc16243b4a0ba1f1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> LCSW | [View](https://www.openjobs-ai.com/jobs/social-worker-lcsw-social-services-full-time-8-hours-day-730am-to-400pmnon-union-non-exempt-arcadia-ca-128391932018688868) |
| Division Chief Cardiology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/74/600f654573f49027007e6836fde04.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Connecticut Children's | [View](https://www.openjobs-ai.com/jobs/division-chief-cardiology-hartford-ct-128391932018688869) |
| Lead Teacher, Tutor Time of Newark | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/e2/397b4198f6a8be20d4d11a9cbe294.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tutor Time Childcare | [View](https://www.openjobs-ai.com/jobs/lead-teacher-tutor-time-of-newark-newark-de-128391932018688870) |
| Inspector I - Building | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/9b/fdf436482f955d5bdaa590e5b342f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> City of Rochester Hills | [View](https://www.openjobs-ai.com/jobs/inspector-i-building-rochester-hills-mi-128391932018688871) |
| Sr. Food Service Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/15/12855e46281f925f5af936a6c3b27.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Boar's Head Brand | [View](https://www.openjobs-ai.com/jobs/sr-food-service-specialist-petersburg-va-128391932018688873) |
| Area Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/f3/b42bf001ae9feb8ce30fc2bb21f30.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Fellowship of Christian Athletes | [View](https://www.openjobs-ai.com/jobs/area-representative-carlsbad-ca-128391932018688874) |
| Maintenance Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/4c/4273204f38c57301de59eb0c003e3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Amcor | [View](https://www.openjobs-ai.com/jobs/maintenance-manager-monroe-la-128391932018688875) |
| RN Registered Nurse PACU | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/5f/c686537741ccdf30cca3d151f29d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HCA Florida Blake Hospital | [View](https://www.openjobs-ai.com/jobs/rn-registered-nurse-pacu-bradenton-fl-128391932018688876) |
| Principal Tax Controversy, Tax Controversy | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/d0/d4809e6bdb6f4db3e547f27b1873c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Amazon | [View](https://www.openjobs-ai.com/jobs/principal-tax-controversy-tax-controversy-seattle-wa-128391932018688877) |
| Human Resources Generalist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/39/e7a2ca27ce39562927de955b11d8d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Select Specialty Hospital | [View](https://www.openjobs-ai.com/jobs/human-resources-generalist-birmingham-al-128391932018688878) |
| Client Service Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/30/d24c9f766c7d68ea60e5c281926f1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ameriprise Financial Services, LLC | [View](https://www.openjobs-ai.com/jobs/client-service-specialist-orlando-fl-128391932018688879) |
| LNA-Licensed Nursing Assistant - Memory Care | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/91/ba3790fe06726cf8da9cd9969db32.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Benchmark Senior Living | [View](https://www.openjobs-ai.com/jobs/lna-licensed-nursing-assistant-memory-care-bedford-nh-128391932018688880) |
| Paralegal | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/9d/00291a3958b3d0bb2cfece0a2fe3a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jobot | [View](https://www.openjobs-ai.com/jobs/paralegal-greenville-sc-128391932018688881) |
| REGISTERED NURSE -MED-SURGE - OBMC-2A- F/T NIGHTS | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/a6/3ff20d68906024431b7de53765c3c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> JFK Johnson Rehabilitation Institute | [View](https://www.openjobs-ai.com/jobs/registered-nurse-med-surge-obmc-2a-ft-nights-old-bridge-nj-128391932018688882) |
| Corporate Accountant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/9d/00291a3958b3d0bb2cfece0a2fe3a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jobot | [View](https://www.openjobs-ai.com/jobs/corporate-accountant-yonkers-ny-128391932018688883) |
| Maintenance Technicians - Multiple Roles & Shifts! | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/9d/00291a3958b3d0bb2cfece0a2fe3a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jobot | [View](https://www.openjobs-ai.com/jobs/maintenance-technicians-multiple-roles-shifts-hoopeston-il-128391932018688884) |
| Onbase Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/c7/2f61aa4e35ae18fdde0458a68f670.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Maayee, Inc. | [View](https://www.openjobs-ai.com/jobs/onbase-developer-suwanee-ga-128391932018688885) |
| Civil Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/9d/00291a3958b3d0bb2cfece0a2fe3a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jobot | [View](https://www.openjobs-ai.com/jobs/civil-engineer-columbus-oh-128391932018688886) |
| Maintenance Tech- Night Shift | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/9d/00291a3958b3d0bb2cfece0a2fe3a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jobot | [View](https://www.openjobs-ai.com/jobs/maintenance-tech-night-shift-granville-oh-128391932018688887) |
| Physician - Urologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/27/8df73d7420e6e291032e7823ddd11.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CHRISTUS Health | [View](https://www.openjobs-ai.com/jobs/physician-urologist-beaumont-tx-128391932018688888) |
| Audit Senior | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/9d/00291a3958b3d0bb2cfece0a2fe3a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jobot | [View](https://www.openjobs-ai.com/jobs/audit-senior-tulsa-ok-128391932018688889) |
| Marketing Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/9d/00291a3958b3d0bb2cfece0a2fe3a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jobot | [View](https://www.openjobs-ai.com/jobs/marketing-manager-tucson-az-128391932018688890) |
| Safety/Environmental Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/65/30c34ddc429713e654a1a5f593a56.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> U.S. Sugar | [View](https://www.openjobs-ai.com/jobs/safetyenvironmental-specialist-clewiston-fl-128391932018688891) |
| Retail Merchandiser | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/d4/ecfd4c29771f1076eda29e4cfc044.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CROSSMARK | [View](https://www.openjobs-ai.com/jobs/retail-merchandiser-collierville-tn-128391932018688892) |
| Lead Electrical Engineer - Industrial | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/9d/00291a3958b3d0bb2cfece0a2fe3a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jobot | [View](https://www.openjobs-ai.com/jobs/lead-electrical-engineer-industrial-alexander-ar-128391932018688893) |
| Entry Level Weekend Jobs Tucson \| Paid Caregiver Training | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/e0/c9b330a8cf6df8790900a959f6d5c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Adultcare Assistance Homecare | [View](https://www.openjobs-ai.com/jobs/entry-level-weekend-jobs-tucson-paid-caregiver-training-tucson-az-128391932018688894) |
| Public Safety Dispatcher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/69/5d76cffba5a02ff560fc89e5dd1c1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mohave County | [View](https://www.openjobs-ai.com/jobs/public-safety-dispatcher-kingman-az-128391932018688895) |
| Product Liability Paralegal | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/9d/00291a3958b3d0bb2cfece0a2fe3a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jobot | [View](https://www.openjobs-ai.com/jobs/product-liability-paralegal-pittsburgh-pa-128391932018688896) |
| Clinical Assessor/Clinician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/eb/3dffff59036b192cf267fe5c6efd8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Progressive Community Services | [View](https://www.openjobs-ai.com/jobs/clinical-assessorclinician-chester-va-128391932018688897) |
| Infrastructure Technical Program Manager, Global Connectivity Infrastructure Delivery - Fiber Deployment | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/17/f09b91594e1b16f374b34593d895d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Amazon Web Services (AWS) | [View](https://www.openjobs-ai.com/jobs/infrastructure-technical-program-manager-global-connectivity-infrastructure-delivery-fiber-deployment-herndon-va-128392942845952000) |
| Law Clerk Internship | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/45/c0d4b56eaa2b83b2e2bba225ae7f4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Colorado Judicial Branch | [View](https://www.openjobs-ai.com/jobs/law-clerk-internship-centennial-co-128392942845952001) |
| Automotive Sales Associate \| Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/da/2eaf9942aa5e41029649bb677ca6c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kings Ford Inc. | [View](https://www.openjobs-ai.com/jobs/automotive-sales-associate-consultant-cincinnati-oh-128392942845952002) |
| First-Line Supervisors of Police and Detectives - AI Trainer (Contract) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/32/2d844424d22d941f0536b7e9c2271.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Handshake | [View](https://www.openjobs-ai.com/jobs/first-line-supervisors-of-police-and-detectives-ai-trainer-contract-united-states-128392942845952003) |
| Clinic Director/Physical Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/ec/7a6ab8efffc24353289839129c762.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Doctors of Physical Therapy | [View](https://www.openjobs-ai.com/jobs/clinic-directorphysical-therapist-phoenix-az-128392942845952004) |
| Director, Tech Lead - AI Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/66/11a12d43fa84348321533d9e969ef.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Prudential Financial | [View](https://www.openjobs-ai.com/jobs/director-tech-lead-ai-engineer-newark-nj-128392942845952005) |
| LMSW LCSW PRN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/4e/67b9271758edace29205a88209e73.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Addus HomeCare | [View](https://www.openjobs-ai.com/jobs/lmsw-lcsw-prn-espanola-nm-128392942845952006) |
| Sales Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/e2/ac41d9af32f041f561fbe42e4c839.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> West500 Partners | [View](https://www.openjobs-ai.com/jobs/sales-engineer-kent-wa-128392942845952007) |
| Seeking CFP professionals with CPA or EA credentials - REMOTE | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/72/b989282376fe513c4e31196484195.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Domain Money | [View](https://www.openjobs-ai.com/jobs/seeking-cfp-professionals-with-cpa-or-ea-credentials-remote-united-states-128392942845952008) |
| Director, PMO - C5ISR | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/5f/380aa02538a4694eb3e0268a7e115.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Vitesse Systems | [View](https://www.openjobs-ai.com/jobs/director-pmo-c5isr-longmont-co-128392942845952009) |
| Sales Coordinator, AllPayer \| Internship \| Remote \| NantHealth | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/61/bfc3dfc1b68d01838476cf30b8051.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NantHealth | [View](https://www.openjobs-ai.com/jobs/sales-coordinator-allpayer-internship-remote-nanthealth-dallas-tx-128392942845952010) |
| Specialized Tax Services - Energy Incentives & Credits Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/specialized-tax-services-energy-incentives-credits-senior-manager-boston-ma-128392942845952011) |
| Specialized Tax Services - Research & Development Tax Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/specialized-tax-services-research-development-tax-senior-manager-washington-dc-128392942845952012) |
| Physical Therapist Assistant (PTA) - PRN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/00/415707e454ea23453fd16687df235.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OVATION Rehabilitation Services, LLC | [View](https://www.openjobs-ai.com/jobs/physical-therapist-assistant-pta-prn-daytona-beach-fl-128392942845952013) |
| Senior Legal Assistant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/71/471e7d76b70069a2ae1e5818fe2d6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bloom Energy | [View](https://www.openjobs-ai.com/jobs/senior-legal-assistant-san-jose-ca-128392942845952014) |
| Account Executive, North America | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/ed/68a21d69409f3a260ef23392b9a2d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Topsort | [View](https://www.openjobs-ai.com/jobs/account-executive-north-america-boston-ma-128392942845952015) |
| Entry-Level Construction Technician - Tampa, FL | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/a5/96fcd7b0a047a960f685075910a6b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> VetJobs | [View](https://www.openjobs-ai.com/jobs/entry-level-construction-technician-tampa-fl-tampa-fl-128392942845952016) |
| Software Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/30/b06b9907198d68f229aeb3e8430cf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Insight Global | [View](https://www.openjobs-ai.com/jobs/software-engineer-united-states-128392942845952017) |
| B2B Sales Account Executive | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/5d/b43f237832cbf0f299bd8f2bcf2ac.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AT&T | [View](https://www.openjobs-ai.com/jobs/b2b-sales-account-executive-el-segundo-ca-128392942845952018) |
| SNF (Skilled Nursing Facility) Rounding MD | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/4e/88b016cea843f427c9a889061231a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Southeast Permanente Medical Group | [View](https://www.openjobs-ai.com/jobs/snf-skilled-nursing-facility-rounding-md-georgia-united-states-128392942845952019) |
| Caregiver | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/e4/ccdae5fae24543a674023f9a7d0a6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Home Instead | [View](https://www.openjobs-ai.com/jobs/caregiver-pocomoke-city-md-128392942845952020) |
| Senior Tax Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/61/ad000a58e4486b14b8f286c6fe507.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> 1Source Partners | [View](https://www.openjobs-ai.com/jobs/senior-tax-associate-tampa-fl-128392942845952021) |
| Controls Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/3f/8de31435ace701b484c4597157aca.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cooper Standard | [View](https://www.openjobs-ai.com/jobs/controls-engineer-surgoinsville-tn-128392942845952022) |
| Embedded Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/9b/6b983f5054ee48c3a5a8cc761eb2d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> InfoVision Inc. | [View](https://www.openjobs-ai.com/jobs/embedded-engineer-dallas-tx-128392942845952023) |
| Certified Nursing Assistant (CNA) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/81/2ab771e5d64e586cacef5aa76a17a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ACG Hospice | [View](https://www.openjobs-ai.com/jobs/certified-nursing-assistant-cna-polk-county-nc-128392942845952024) |
| Machine Learning Software Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/5d/27128c070b26354e4b96d78f1ed74.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Aimhire | [View](https://www.openjobs-ai.com/jobs/machine-learning-software-engineer-united-states-128392942845952025) |
| Montessori Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/c6/2b60badb460cf418710eaf6d98cf2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cadence Education | [View](https://www.openjobs-ai.com/jobs/montessori-director-gilbert-az-128392942845952026) |
| Sales Capability Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/26/2be313467a4ce3ec02c8ee6535ffb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CDW | [View](https://www.openjobs-ai.com/jobs/sales-capability-advisor-tampa-fl-128392942845952027) |
| Front of House Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/bc/96108462f8a75573df8ac23c32989.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PharmaCann Inc | [View](https://www.openjobs-ai.com/jobs/front-of-house-manager-romeoville-il-128392942845952028) |
| Material Handler III Packing | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/98/8e7c255ca881762cc672ad04415d9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Brodart | [View](https://www.openjobs-ai.com/jobs/material-handler-iii-packing-williamsport-pa-128392942845952029) |
| Warehouse Operations Manager – Production / Light Assembly | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/08/69c9df16c05ce98a5e13ef84f7006.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> IndiMade Brands | [View](https://www.openjobs-ai.com/jobs/warehouse-operations-manager-production-light-assembly-independence-oh-128392942845952030) |
| Bilingual HR Risk and Compliance Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/58/30c5a2b590301a4cd5b78b6211ec3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Addison Group | [View](https://www.openjobs-ai.com/jobs/bilingual-hr-risk-and-compliance-specialist-cypress-tx-128392942845952032) |
| Agile PM | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/e0/8facf91aa3419ad4bce010959608d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Client Resources, Inc. | [View](https://www.openjobs-ai.com/jobs/agile-pm-omaha-ne-128392942845952033) |
| Surveillance Investigator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/a7/186115ffcebc959f78f3a9b7562cf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DigiStream Investigations | [View](https://www.openjobs-ai.com/jobs/surveillance-investigator-united-states-128392942845952034) |
| Packaging Sales Executive | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/6d/040d5b3530856b7ff36d25563c450.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NPAworldwide | [View](https://www.openjobs-ai.com/jobs/packaging-sales-executive-austin-tx-128392942845952035) |
| Territory Sales Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/10/efb2ac5710215b0a5d13fe7e705b8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The N2 Company | [View](https://www.openjobs-ai.com/jobs/territory-sales-manager-minnetonka-mn-128392942845952036) |
| Nephrology Nurse RN Educator-Coordinator kidney care preferred | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/4c/78cff44e309435774f26de659ec12.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ChenMed | [View](https://www.openjobs-ai.com/jobs/nephrology-nurse-rn-educator-coordinator-kidney-care-preferred-miami-fl-128392942845952037) |
| Floor Tech | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/ad/9ad51feb92d1ab813cddef8241a00.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Infinite Care Consulting Services | [View](https://www.openjobs-ai.com/jobs/floor-tech-kingston-ny-128392942845952038) |
| Sales Counselor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/07/53d2276fa75c06c6a855718f24a7e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Everstory Partners | [View](https://www.openjobs-ai.com/jobs/sales-counselor-tampa-fl-128392942845952039) |
| Senior Mortgage Loan Officer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/fb/90b70123c2cc35f6888c88bb4e046.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> American National Bank of Texas | [View](https://www.openjobs-ai.com/jobs/senior-mortgage-loan-officer-hurst-tx-128392942845952040) |
| Director of Nursing - Bishop Spencer Place | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/9a/c9e9f895f79ba7f4847d059ea9a3f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Saint Luke's | [View](https://www.openjobs-ai.com/jobs/director-of-nursing-bishop-spencer-place-kansas-city-metropolitan-area-128392942845952042) |
| Finance Operations, Insurance- Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/finance-operations-insurance-senior-associate-boston-ma-128392942845952043) |
| Forward Deployed Software Engineer-Palantir Foundry-Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/forward-deployed-software-engineer-palantir-foundry-director-miami-fl-128392942845952044) |
| Specialized Tax Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Research & Development Tax | [View](https://www.openjobs-ai.com/jobs/specialized-tax-services-research-development-tax-senior-associate-washington-dc-128392942845952045) |
| SAP EWM  Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/sap-ewm-manager-baltimore-md-128392942845952046) |
| Risk Modeling Services P&C - Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/risk-modeling-services-pc-senior-associate-cincinnati-oh-128392942845952047) |
| Ambulatory RN - Pulmonary | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/fd/87e099ca4630b42393bb3f9f936c9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Trinity Health | [View](https://www.openjobs-ai.com/jobs/ambulatory-rn-pulmonary-muskegon-mi-128392942845952048) |
| Associate Financial Advisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/52/f810d66ee6b9ab2c69acfe5cac707.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> GemHarvest Executive Recruiting | [View](https://www.openjobs-ai.com/jobs/associate-financial-advisor-greater-philadelphia-128392942845952049) |
| Mental Health Professional Hourly | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/c5/09236eb57a3142af62e7383ac3da3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Wellpath | [View](https://www.openjobs-ai.com/jobs/mental-health-professional-hourly-elkhart-in-128392942845952050) |
| Assistant, Medical II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/5d/0aac9b091e8a1c001ab78acce07fa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kaiser Permanente | [View](https://www.openjobs-ai.com/jobs/assistant-medical-ii-atlanta-ga-128392942845952051) |
| Nurse Manager Utilization Management | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/98/10a509c6e0226814c157849db53f5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kaiser Permanente Northwest | [View](https://www.openjobs-ai.com/jobs/nurse-manager-utilization-management-portland-or-128392942845952052) |
| Dietetic Assistant-Chilton Medical Center-Per Diem | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/c2/bbd4137619b5bda8a3677e3afd256.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Atlantic Health | [View](https://www.openjobs-ai.com/jobs/dietetic-assistant-chilton-medical-center-per-diem-new-jersey-united-states-128392942845952053) |
| Filler Operator 3rd Shift - $21.00 PLUS 15% Shift Differential | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/91/cbaa7b4127610b59e69661d5d6b9f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lactalis American Group | [View](https://www.openjobs-ai.com/jobs/filler-operator-3rd-shift-2100-plus-15-shift-differential-brattleboro-vt-128392942845952054) |
| Satellite Housing Navigator (Case Manager) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/b0/7a3e67592da89726cf0f622166339.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Community Teamwork | [View](https://www.openjobs-ai.com/jobs/satellite-housing-navigator-case-manager-lowell-ma-128392942845952055) |
| Vice President Operations | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/32/7dfbf65b344292358a27e87d2aa39.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Noto Group | [View](https://www.openjobs-ai.com/jobs/vice-president-operations-springfield-mo-128392942845952056) |
| Z/OS Systems Administrator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/db/60f155e4f2cab66ecaffd8fbd0bcb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Odyssey Information Services | [View](https://www.openjobs-ai.com/jobs/zos-systems-administrator-plano-tx-128392942845952057) |
| Financial Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/ec/ed0e3708955eb31a379d65212dc81.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> We Insure | [View](https://www.openjobs-ai.com/jobs/financial-analyst-austin-tx-128392942845952058) |
| Website Performance Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/b5/7bdb309927848387eecc6289b1d42.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Team Velocity | [View](https://www.openjobs-ai.com/jobs/website-performance-manager-united-states-128392942845952059) |
| Senior Business Account Executive, SMB Direct Sales (Outside Sales) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/8b/58f7bfce28eefcc1cdd5b95c3b663.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Comcast | [View](https://www.openjobs-ai.com/jobs/senior-business-account-executive-smb-direct-sales-outside-sales-memphis-tn-128392942845952060) |
| Life Skills Trainer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/66/a6aca6a4489f87ea52eb8e6e81559.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Collage Rehabilitation Partners | [View](https://www.openjobs-ai.com/jobs/life-skills-trainer-richmond-va-128392942845952061) |
| ENGINEER PLANNING ANALYST 4 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/5e/a705ca1ff21e0ae36a8d0fc3925e4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Newport News Shipbuilding, A Division of HII | [View](https://www.openjobs-ai.com/jobs/engineer-planning-analyst-4-newport-news-va-128392942845952062) |
| Secondary Operator (2nd/3rd Shift) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/26/f969347226cee3320e9e82a86a47c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PennEngineering® | [View](https://www.openjobs-ai.com/jobs/secondary-operator-2nd3rd-shift-waterford-mi-128392942845952063) |

<p align="center">
  <em>...and 779 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated January 27, 2026
</p>
