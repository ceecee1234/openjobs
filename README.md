<p align="center">
  <img src="https://img.shields.io/badge/jobs-37+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-27+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 27+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 15 |
| Healthcare | 9 |
| Management | 6 |
| Engineering | 3 |
| Sales | 2 |
| Marketing | 1 |
| Operations | 1 |
| Finance | 0 |
| HR | 0 |

**Top Hiring Companies:** State of Oklahoma, IQVIA, Google, Cognizant, Accenture

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
│  │ Sitemap     │   │ (37+ jobs) │   │ (README + HTML)     │   │
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
- **And 27+ other companies**

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
  <em>Updated February 23, 2026 · Showing 37 of 37+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Account Executive | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/f9/dcaf56ac562980285c306aaf6d17f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kensington Partners Group | [View](https://www.openjobs-ai.com/jobs/account-executive-boise-id-138178879029248004) |
| Servicing Transfer Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/a3/5f5822521465f8679e995a80c7f84.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cornerstone Servicing | [View](https://www.openjobs-ai.com/jobs/servicing-transfer-associate-englewood-co-138178879029248005) |
| Analyst AP 2 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/eb/664c982b4278b48573cda56d0bd6f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Daikin Comfort | [View](https://www.openjobs-ai.com/jobs/analyst-ap-2-chesterfield-mo-138179021635584000) |
| RN / Registered Nurse - Hospice | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/d9/54ccb9e0f549974eba51e8db8a6be.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Allay Hospice | [View](https://www.openjobs-ai.com/jobs/rn-registered-nurse-hospice-jackson-wi-138179021635584001) |
| Patient Transporter | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/56/25193c22e01bbce91e2f54446ed78.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Corewell Health | [View](https://www.openjobs-ai.com/jobs/patient-transporter-troy-mi-138179021635584002) |
| Coder II Professional Fee | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/4a/bb74028d722f1149047dc9788c0a0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CommonSpirit Health | [View](https://www.openjobs-ai.com/jobs/coder-ii-professional-fee-englewood-co-138179298459648000) |
| Clinical Research Associate, Sponsor Dedicated | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/49/74f8eed435f594de307c71ed324e0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> IQVIA | [View](https://www.openjobs-ai.com/jobs/clinical-research-associate-sponsor-dedicated-el-cajon-ca-138178677702656009) |
| Consulting Manager [Utilities-Customer Operations exp.], (Utilities Global Advisory Consulting Practice) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/f7/e09886607fea2f31b199746e2cde7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cognizant | [View](https://www.openjobs-ai.com/jobs/consulting-manager-utilities-customer-operations-exp-utilities-global-advisory-consulting-practice-harleysville-pa-138178677702656010) |
| Internship Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/bd/0af296d2accffa31c97e0436f50d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Arc San Francisco | [View](https://www.openjobs-ai.com/jobs/internship-coordinator-san-francisco-ca-138178677702656011) |
| Industry X - Digital Manufacturing Architecture Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/96/a479c49f59f0f9e66875d0d856ab6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Accenture | [View](https://www.openjobs-ai.com/jobs/industry-x-digital-manufacturing-architecture-senior-manager-albany-new-york-metropolitan-area-138178677702656012) |
| $1500 Sign On Bonus - Social Worker (Bachelor of Social Work) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/62/6bd145eb02489631bc81aff265837.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Suncrest Hospice | [View](https://www.openjobs-ai.com/jobs/1500-sign-on-bonus-social-worker-bachelor-of-social-work-san-rafael-ca-138178677702656013) |
| Field Sales Representative, Greenfield, Google Cloud | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/82/2c1b63853ed273b89687ac505f9fa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Google | [View](https://www.openjobs-ai.com/jobs/field-sales-representative-greenfield-google-cloud-ohio-united-states-138178677702656014) |
| Vice President of 3(16) Fiduciary Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/0c/7eca98dd31913097fd653455be771.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Definiti LLC | [View](https://www.openjobs-ai.com/jobs/vice-president-of-316-fiduciary-services-united-states-138178677702656015) |
| RN Director Home Health | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/eb/23e54edfbfec5ca710b8bddc6ae46.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Elios Talent | [View](https://www.openjobs-ai.com/jobs/rn-director-home-health-houston-tx-138178677702656016) |
| Stability LIMS Systems Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/a5/eb62450fe2a1ffd60146db07d2364.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Thermo Fisher Scientific | [View](https://www.openjobs-ai.com/jobs/stability-lims-systems-specialist-new-brunswick-nj-138178677702656017) |
| Contract Specialist (Austin) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/8a/5809b5b85688e542b67b945a8767b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Texas Workforce Commission | [View](https://www.openjobs-ai.com/jobs/contract-specialist-austin-austin-tx-138178677702656018) |
| Clinical Research Associate, Sponsor Dedicated | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/49/74f8eed435f594de307c71ed324e0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> IQVIA | [View](https://www.openjobs-ai.com/jobs/clinical-research-associate-sponsor-dedicated-lawton-ok-138178677702656019) |
| Clinical Research Associate, Sponsor Dedicated | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/49/74f8eed435f594de307c71ed324e0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> IQVIA | [View](https://www.openjobs-ai.com/jobs/clinical-research-associate-sponsor-dedicated-belmar-nj-138178677702656020) |
| Marketing Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/99/c4e6e382cd8790997a83ac2a4a07f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Metrology | [View](https://www.openjobs-ai.com/jobs/marketing-specialist-metrology-san-francisco-san-francisco-ca-138178677702656021) |
| Temporary Laborer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/9d/2272d68646cf8d1c8a1266aafade7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> State of Oklahoma | [View](https://www.openjobs-ai.com/jobs/temporary-laborer-oklahoma-county-ok-138178677702656022) |
| Agent - Medicaid Fraud Control | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/9d/2272d68646cf8d1c8a1266aafade7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> State of Oklahoma | [View](https://www.openjobs-ai.com/jobs/agent-medicaid-fraud-control-oklahoma-county-ok-138178677702656023) |
| Senior Account Manager / Account Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/39/6cf94b5cc278e4edd0b3ecb15af57.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ottomatik.io | [View](https://www.openjobs-ai.com/jobs/senior-account-manager-account-director-latin-america-138178677702656024) |
| Sr. Consultant [Utilities-Field Operations exp.], (Utilities Global Advisory Consulting Practice) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/f7/e09886607fea2f31b199746e2cde7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cognizant | [View](https://www.openjobs-ai.com/jobs/sr-consultant-utilities-field-operations-exp-utilities-global-advisory-consulting-practice-new-york-ny-138178677702656025) |
| Scientist / Senior Scientist, DMPK | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/c6/6bab592e52e377f84fbb6c3218257.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Altos Labs | [View](https://www.openjobs-ai.com/jobs/scientist-senior-scientist-dmpk-san-francisco-ca-138178677702656027) |
| Fire Prevention & Security Officer I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/9d/2272d68646cf8d1c8a1266aafade7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> State of Oklahoma | [View](https://www.openjobs-ai.com/jobs/fire-prevention-security-officer-i-tulsa-ok-138178677702656028) |
| Program Manager, Data Information Systems | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/9d/2272d68646cf8d1c8a1266aafade7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> State of Oklahoma | [View](https://www.openjobs-ai.com/jobs/program-manager-data-information-systems-oklahoma-county-ok-138178677702656029) |
| Neonatal Intensive Care Unit Respiratory Therapist Tampa | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/08/9a72c48bbf0ef2890317158be3530.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AdventHealth | [View](https://www.openjobs-ai.com/jobs/neonatal-intensive-care-unit-respiratory-therapist-tampa-tampa-fl-138178677702656030) |
| Technical Program Manager, Data Center Security and Compliance | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/82/2c1b63853ed273b89687ac505f9fa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Google | [View](https://www.openjobs-ai.com/jobs/technical-program-manager-data-center-security-and-compliance-the-dalles-or-138178677702656031) |
| Technical Program Manager III, Data Center Design | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/82/2c1b63853ed273b89687ac505f9fa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Google | [View](https://www.openjobs-ai.com/jobs/technical-program-manager-iii-data-center-design-pryor-ok-138178677702656032) |
| Social Worker II - Department of Family and Children Services (DFCS) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/9e/ed6d563bb2cf89cd58397b76e1534.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> County of Santa Clara | [View](https://www.openjobs-ai.com/jobs/social-worker-ii-department-of-family-and-children-services-dfcs-santa-clara-county-ca-138178677702656033) |
| 3(16) Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/0c/7eca98dd31913097fd653455be771.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Definiti LLC | [View](https://www.openjobs-ai.com/jobs/316-consultant-united-states-138178677702656034) |
| Senior Customer Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/40d2be1c71c89f91ab04a5b46b9fc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Collibra | [View](https://www.openjobs-ai.com/jobs/senior-customer-engineer-chicago-il-138178677702656035) |
| Residency Program - New Nurse Graduates | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/25/fdf5c5d48111aedbf1d70ee1845f9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BAYADA Home Health Care | [View](https://www.openjobs-ai.com/jobs/residency-program-new-nurse-graduates-indiana-pa-138178677702656036) |
| CAD Engineer - PDV | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/f3/870be274f6c49b3e31a0c6728957f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Apple | [View](https://www.openjobs-ai.com/jobs/cad-engineer-pdv-austin-tx-138178677702656037) |
| Behavioral Health Case Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/be/8764163a3154417c9486cf5babd66.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ascension | [View](https://www.openjobs-ai.com/jobs/behavioral-health-case-manager-hoffman-estates-il-138178879029248000) |
| Project Senior Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/96/a479c49f59f0f9e66875d0d856ab6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Accenture | [View](https://www.openjobs-ai.com/jobs/project-senior-analyst-irving-tx-138178879029248001) |
| General Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/6c/d5c599dd36a74b4678923802252fe.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Zamp | [View](https://www.openjobs-ai.com/jobs/general-manager-charlotte-nc-138178879029248002) |

<p align="center">
  <em>...and 0 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated February 23, 2026
</p>
