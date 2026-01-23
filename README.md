<p align="center">
  <img src="https://img.shields.io/badge/jobs-749+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-495+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 495+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 236 |
| Management | 184 |
| Healthcare | 161 |
| Engineering | 86 |
| Sales | 43 |
| Finance | 26 |
| Operations | 6 |
| Marketing | 5 |
| HR | 2 |

**Top Hiring Companies:** PwC, Vibra Healthcare, Meta, Sevita, Oracle

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
│  │ Sitemap     │   │ (749+ jobs) │   │ (README + HTML)     │   │
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
- **And 495+ other companies**

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
  <em>Updated January 23, 2026 · Showing 200 of 749+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Research Scientist Intern, AI Research - Multimodal Pretraining (PhD) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/9a/23cbc455158951716b440c3d165e0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Meta | [View](https://www.openjobs-ai.com/jobs/research-scientist-intern-ai-research-multimodal-pretraining-phd-menlo-park-ca-127319276519425141) |
| Div 10 Project Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/cb/09f3bf2d27e0c00b9de5e0738f0b2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> APTURA GROUP | [View](https://www.openjobs-ai.com/jobs/div-10-project-manager-indianapolis-in-127319276519425142) |
| Physical Therapist - Outpatient | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/89/39d75e6682e401254ac51423968ab.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bonsai Rehab | [View](https://www.openjobs-ai.com/jobs/physical-therapist-outpatient-eureka-mo-127319276519425143) |
| PT- Medication Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/ea/2946be6fac74ead98638a99078b2b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MBK Senior Living | [View](https://www.openjobs-ai.com/jobs/pt-medication-technician-petaluma-ca-127319276519425144) |
| Pharmacy Technician I | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/01/6b469c2071eef5856ef57a5cd3c19.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kaleida Health | [View](https://www.openjobs-ai.com/jobs/pharmacy-technician-i-buffalo-ny-127319276519425145) |
| Welder Apprentice | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/43/c343340e48e1d2554c231309ff0cb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AERZEN USA | [View](https://www.openjobs-ai.com/jobs/welder-apprentice-greeneville-tn-127319276519425146) |
| Bus Cleaner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/1a/d52bd7e1bc0c3e4081c1ac6c3120c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Complete Coach Works | [View](https://www.openjobs-ai.com/jobs/bus-cleaner-von-ormy-tx-127319276519425147) |
| Dining Room Supervisor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/ea/2946be6fac74ead98638a99078b2b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MBK Senior Living | [View](https://www.openjobs-ai.com/jobs/dining-room-supervisor-san-clemente-ca-127319276519425148) |
| Associate Neurophysiologist (Rockford, IL) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/ea/ff5ae9a836c08bb57beaa701dc658.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Globus Medical | [View](https://www.openjobs-ai.com/jobs/associate-neurophysiologist-rockford-il-illinois-united-states-127319276519425149) |
| Production Engineer (University Grad) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/9a/23cbc455158951716b440c3d165e0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Meta | [View](https://www.openjobs-ai.com/jobs/production-engineer-university-grad-bellevue-wa-127319276519425150) |
| RN Patient Nurse Navigator, Spine | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/89/dde9ea2c93928721a8830796f5eb4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Atrium Health Wake Forest Baptist | [View](https://www.openjobs-ai.com/jobs/rn-patient-nurse-navigator-spine-clemmons-nc-127319276519425151) |
| Community Home Care: RN Case Manager (South Metro) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/8b/ba2e6b5edc2bc819be178bfc6d6bf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lifespark | [View](https://www.openjobs-ai.com/jobs/community-home-care-rn-case-manager-south-metro-st-louis-park-mn-127319276519425152) |
| Senior Accountant / FP&A Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/67/2b8256393b44804db1b4ec938e3d0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CFS | [View](https://www.openjobs-ai.com/jobs/senior-accountant-fpa-analyst-baltimore-md-127319276519425153) |
| Specialty Pharmacy Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/43/73b38c70cf7ed87e387a547fc6205.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Shields Health Solutions | [View](https://www.openjobs-ai.com/jobs/specialty-pharmacy-technician-aurora-co-127319276519425155) |
| Signage Installer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/40/686eecd46ef28bd1fee319cec24e8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SpeedPro Omaha | [View](https://www.openjobs-ai.com/jobs/signage-installer-omaha-ne-127319276519425156) |
| Head of Human Resources | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/10/e53dfc365ca6dcc508baead564d5c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PEPL | [View](https://www.openjobs-ai.com/jobs/head-of-human-resources-tampa-fl-127319276519425157) |
| Real Estate Valuations Services Manager or Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/58/058d8987e7a9ec723bcdbec6c407e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Weaver | [View](https://www.openjobs-ai.com/jobs/real-estate-valuations-services-manager-or-senior-manager-denver-co-127319276519425158) |
| Digital Business Development Director - North America | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/1e/1f8b6379167b93774686718038db4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Framework | [View](https://www.openjobs-ai.com/jobs/digital-business-development-director-north-america-washington-dc-baltimore-area-127319276519425159) |
| Registered Respiratory Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/a1/290af73f272b6a2c3a074e7986964.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cabell Huntington Hospital | [View](https://www.openjobs-ai.com/jobs/registered-respiratory-therapist-point-pleasant-wv-127319276519425160) |
| Middle School ELA Support | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/af/651536fe9c73d6179b21dc68424eb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PRACTICE | [View](https://www.openjobs-ai.com/jobs/middle-school-ela-support-brooklyn-ny-127319276519425161) |
| Administrative Budget Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/57/0bdd05aabd4a3d4972ed6a1409a49.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> City of New York | [View](https://www.openjobs-ai.com/jobs/administrative-budget-analyst-manhattan-ny-127319276519425162) |
| Arizona Serve VISTA - VISTA Team Leader | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/04/8f77447036ca7e6fdf01b0358f6db.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AmeriCorps | [View](https://www.openjobs-ai.com/jobs/arizona-serve-vista-vista-team-leader-tucson-az-127319276519425163) |
| Corporate Development Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/dc/984e2aef527ea2daaeffe646a6a52.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AMD | [View](https://www.openjobs-ai.com/jobs/corporate-development-senior-manager-santa-clara-ca-127319276519425164) |
| Program Coordinator - General Medicine | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/10/d3ea49aae7cd54da26a3f6c989035.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Columbia University Irving Medical Center | [View](https://www.openjobs-ai.com/jobs/program-coordinator-general-medicine-new-york-ny-127319276519425165) |
| Senior Binding Authority Underwriting Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/16/a6d586590025e0f658b0f176bf76d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ryan Specialty | [View](https://www.openjobs-ai.com/jobs/senior-binding-authority-underwriting-associate-worthington-oh-127319276519425166) |
| Structural PE | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/ce/724fd56fce4d0aeff77673158f30e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Wallace Design Collective | [View](https://www.openjobs-ai.com/jobs/structural-pe-nashville-tn-127319276519425167) |
| Supervisor - Bridges Program | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fb/881bf3e57eb8b3449a49aacbd9a48.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MultiCare Health System | [View](https://www.openjobs-ai.com/jobs/supervisor-bridges-program-tacoma-wa-127319276519425168) |
| FY26 US Seasonal Tax-Financial Services Organization-Wealth and Asset Management Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/13/9fe096ac3abc5eb9438fae1dd49d1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> EY | [View](https://www.openjobs-ai.com/jobs/fy26-us-seasonal-tax-financial-services-organization-wealth-and-asset-management-manager-las-vegas-nv-127319276519425169) |
| Intake Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/d6/1112a2a66189f17b39e705f16faf7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AdaptHealth | [View](https://www.openjobs-ai.com/jobs/intake-specialist-united-states-127321025544192000) |
| Director of Product Marketing | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/9b/552f9f2bc14c85a627107ede62b42.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Fluidra North America | [View](https://www.openjobs-ai.com/jobs/director-of-product-marketing-atlanta-ga-127321025544192001) |
| Financial Services Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/82/2407c4cb46235f6ff6cdd3e254fbe.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bankers Life | [View](https://www.openjobs-ai.com/jobs/financial-services-professional-tulsa-ok-127321025544192002) |
| Surgical Technologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/cf/cdbfd20f03eb342877ff91b76567e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> United Surgical Partners International, Inc | [View](https://www.openjobs-ai.com/jobs/surgical-technologist-austin-tx-127321025544192003) |
| Postdoctoral Fellow - Computational and Quantitative Medicine | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/8c/e9c7eadb85bdcfaba3117ad5a2d84.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> City of Hope | [View](https://www.openjobs-ai.com/jobs/postdoctoral-fellow-computational-and-quantitative-medicine-monrovia-ca-127321025544192004) |
| Physical Therapist - Outpatient | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/89/39d75e6682e401254ac51423968ab.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bonsai Rehab | [View](https://www.openjobs-ai.com/jobs/physical-therapist-outpatient-waxahachie-tx-127321025544192005) |
| Medical Assistant/Receptionist FT 680 Cardio Paterson | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/1e/6d8640bf782ca919dc2b6938da603.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Englewood Hospital | [View](https://www.openjobs-ai.com/jobs/medical-assistantreceptionist-ft-680-cardio-paterson-paterson-nj-127321025544192006) |
| No Experience Needed | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/45/c408256602c7af32f4f6bdeb446b8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Behavior Technician | [View](https://www.openjobs-ai.com/jobs/no-experience-needed-behavior-technician-help-kids-with-autism-clarksville-tn-127321025544192007) |
| Senior Project Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/57/0bdd05aabd4a3d4972ed6a1409a49.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> City of New York | [View](https://www.openjobs-ai.com/jobs/senior-project-manager-queens-ny-127321025544192008) |
| Hospice RN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/53/d85391aec2aa5f2a9933b125690a8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Compassus | [View](https://www.openjobs-ai.com/jobs/hospice-rn-savannah-ga-127321025544192009) |
| Senior Product Manager \| Sage Home Loans | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/00/cf3b0a237d43ade4099ba01b8e126.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sage Home Loans Corporation | [View](https://www.openjobs-ai.com/jobs/senior-product-manager-sage-home-loans-charlotte-nc-127321025544192010) |
| Physical Therapist - Outpatient | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/89/39d75e6682e401254ac51423968ab.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bonsai Rehab | [View](https://www.openjobs-ai.com/jobs/physical-therapist-outpatient-denham-springs-la-127321025544192011) |
| Post Closing Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/00/24ebc258d2b5861de069e0a83856a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HomeXpress Mortgage Corp | [View](https://www.openjobs-ai.com/jobs/post-closing-analyst-santa-ana-ca-127321025544192012) |
| Physical Therapy Assistant-Pool-Weekend Rotation | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/a4/3270b1c58f3ba32a363675028c54e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Unity Health | [View](https://www.openjobs-ai.com/jobs/physical-therapy-assistant-pool-weekend-rotation-searcy-ar-127321025544192013) |
| Senior Scientist / Associate Principal Scientist, Chemical Engineering R&D | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/f4/2496345318ea8af2f9e83066a308e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pharmaron | [View](https://www.openjobs-ai.com/jobs/senior-scientist-associate-principal-scientist-chemical-engineering-rd-coventry-ri-127321025544192014) |
| Veterinary Technician - Floater | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/7b/309e78447acaf7f5bdd8cc56f4b23.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NVA General Practice | [View](https://www.openjobs-ai.com/jobs/veterinary-technician-floater-los-angeles-ca-127321025544192015) |
| Credit and Collections Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/95/022ab9f539645428ce826a48fff9d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Vishay Siliconix Itzehoe GmbH | [View](https://www.openjobs-ai.com/jobs/credit-and-collections-analyst-malvern-pa-127321025544192018) |
| Maternal-Fetal Medicine Physician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/6c/5d89e96ea38e9fe35648c909a5130.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tal Healthcare | [View](https://www.openjobs-ai.com/jobs/maternal-fetal-medicine-physician-brooklyn-ny-127321025544192019) |
| Direct Sales Representative- Residential - $5,000 Sign-On Bonus | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/5f/6ad49085345b194fe3b866425bd1f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Wave Broadband | [View](https://www.openjobs-ai.com/jobs/direct-sales-representative-residential-5000-sign-on-bonus-dallas-tx-127321025544192020) |
| Occupational Therapist/CHT - Outpatient | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/89/39d75e6682e401254ac51423968ab.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bonsai Rehab | [View](https://www.openjobs-ai.com/jobs/occupational-therapistcht-outpatient-layton-ut-127321025544192021) |
| Director, Silicon Photonics Design | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/dc/984e2aef527ea2daaeffe646a6a52.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AMD | [View](https://www.openjobs-ai.com/jobs/director-silicon-photonics-design-san-jose-ca-127321025544192022) |
| Full Stack Senior Software Engineer - Post Trade Systems | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/8b/38bcbe603c320a88ecd4c31c19f21.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> KKR | [View](https://www.openjobs-ai.com/jobs/full-stack-senior-software-engineer-post-trade-systems-boston-ma-127321025544192023) |
| Sales Development Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/18/9c633d9995e11bf8607170ec9a4b8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Santa Monica | [View](https://www.openjobs-ai.com/jobs/sales-development-representative-santa-monica-june-2026-santa-monica-ca-127321025544192024) |
| Core Enterprise Account Executive EST/CST - Remote Maryland | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/6c/c112004f6e530291f74d193a0c0b4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Samsara | [View](https://www.openjobs-ai.com/jobs/core-enterprise-account-executive-estcst-remote-maryland-maryland-united-states-127321025544192025) |
| Staff Software Engineer I - Mobile | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/4e/ace716093461cb79037da6061f443.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Spring Health | [View](https://www.openjobs-ai.com/jobs/staff-software-engineer-i-mobile-new-york-city-metropolitan-area-127321025544192026) |
| Senior Java Software Developer - Backend | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/18/9c633d9995e11bf8607170ec9a4b8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Oracle | [View](https://www.openjobs-ai.com/jobs/senior-java-software-developer-backend-nashville-tn-127321025544192027) |
| Core Enterprise Account Executive EST/CST - Remote Pennsylvania | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/6c/c112004f6e530291f74d193a0c0b4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Samsara | [View](https://www.openjobs-ai.com/jobs/core-enterprise-account-executive-estcst-remote-pennsylvania-pennsylvania-united-states-127321025544192028) |
| Sr. Process Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/be/abde4f313ed47782cfa69bb6d5725.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Corning Incorporated | [View](https://www.openjobs-ai.com/jobs/sr-process-engineer-harrodsburg-ky-127321025544192029) |
| Director Product Marketing, Client Reporting | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/0b/067e20dde2919de8836c310f37352.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Omada Health | [View](https://www.openjobs-ai.com/jobs/director-product-marketing-client-reporting-united-states-127321025544192030) |
| Per Diem pelvic floor trained Physical Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/1f/376c3c6e9e3f59dcfa3377163d1f6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AccordCare | [View](https://www.openjobs-ai.com/jobs/per-diem-pelvic-floor-trained-physical-therapist-sanford-fl-127321025544192031) |
| Senior Accountant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/3b/9f2ba9720886a611712a1777f87a5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Range | [View](https://www.openjobs-ai.com/jobs/senior-accountant-mclean-va-127321025544192032) |
| Digital IC Design Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/10/19c7a2fa7caa73285924e0b39d04d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Analog Devices | [View](https://www.openjobs-ai.com/jobs/digital-ic-design-engineer-wilmington-ma-127321025544192033) |
| Registered Nurse, Home Health | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/be/e2db445ab9caf54973d2c3d730de2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CenterWell Home Health | [View](https://www.openjobs-ai.com/jobs/registered-nurse-home-health-san-angelo-tx-127321025544192034) |
| Oracle HCM Integration and Reporting Lead (Manager) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/26/b45e682edd909737813f44b3b3ca8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Grant Thornton (US) | [View](https://www.openjobs-ai.com/jobs/oracle-hcm-integration-and-reporting-lead-manager-minneapolis-mn-127321025544192035) |
| Technical Support Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/55/f02738dc4edbb33554b7c94fc490e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Celero Commerce | [View](https://www.openjobs-ai.com/jobs/technical-support-representative-dallas-tx-127321025544192036) |
| Supplier Development Engineer, Special Processes | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/51/8b8450327cfd64b0287071be2e796.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hadrian | [View](https://www.openjobs-ai.com/jobs/supplier-development-engineer-special-processes-los-angeles-ca-127321025544192037) |
| Camp Program Specialists and Managers | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/c8/1b053f28e0bb55dd29cb7787ac45b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Girl Scouts River Valleys | [View](https://www.openjobs-ai.com/jobs/camp-program-specialists-and-managers-st-paul-mn-127321025544192038) |
| Production Operator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/db/4b297329fc0cd4deef64f90fd0d87.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lamb Weston | [View](https://www.openjobs-ai.com/jobs/production-operator-boardman-or-127321025544192039) |
| Senior Java Software Developer - Backend | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/18/9c633d9995e11bf8607170ec9a4b8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Oracle | [View](https://www.openjobs-ai.com/jobs/senior-java-software-developer-backend-austin-tx-127321025544192040) |
| Oracle HCM Integration and Reporting Lead (Manager) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/26/b45e682edd909737813f44b3b3ca8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Grant Thornton (US) | [View](https://www.openjobs-ai.com/jobs/oracle-hcm-integration-and-reporting-lead-manager-milwaukee-wi-127321025544192041) |
| Commercial Enterprise Account Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/1a/1a6f05d335df1eac43ffb023c5aad.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HUB International | [View](https://www.openjobs-ai.com/jobs/commercial-enterprise-account-manager-pasco-wa-127321025544192042) |
| WGAL Technical/Engineering Intern - 2026 Summer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/3b/0b35223039cc4d50398c4413fe8e5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> WGAL 8 TV | [View](https://www.openjobs-ai.com/jobs/wgal-technicalengineering-intern-2026-summer-lancaster-pa-127321025544192043) |
| Director of Operations Primary Care | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/d6/ded653c425985d6e83f30e34077a4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Samaritan Healthcare | [View](https://www.openjobs-ai.com/jobs/director-of-operations-primary-care-moses-lake-wa-127321025544192044) |
| Advanced Practice Professional: Urology, Wheeling, WV | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/00/1511322ed0675a3189328643615a3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> WVU Medicine | [View](https://www.openjobs-ai.com/jobs/advanced-practice-professional-urology-wheeling-wv-wheeling-wv-127321025544192045) |
| IPORT General Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/c7/abb65c6c886620d1eee13e918b68b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sonance | [View](https://www.openjobs-ai.com/jobs/iport-general-manager-san-clemente-ca-127321025544192046) |
| Sales Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/9b/f0a530edd31366cb935780800c67a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Victra | [View](https://www.openjobs-ai.com/jobs/sales-consultant-ogallala-ne-127321025544192047) |
| Territory Business Manager - Neuromuscular (Boston, MA) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/4b/a4b80b3c7c8a74242014202aa3ced.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Takeda | [View](https://www.openjobs-ai.com/jobs/territory-business-manager-neuromuscular-boston-ma-united-states-127321025544192048) |
| Territory Business Manager - Neuromuscular (Boston, MA) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/4b/a4b80b3c7c8a74242014202aa3ced.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Takeda | [View](https://www.openjobs-ai.com/jobs/territory-business-manager-neuromuscular-boston-ma-boston-ma-127321025544192049) |
| Music Teacher Store 334 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/ce/b26d66003463af5b483194bbbe6c1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Guitar Center Company | [View](https://www.openjobs-ai.com/jobs/music-teacher-store-334-chicago-il-127321025544192050) |
| Radiologic Technologist Lead Mammo | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/5d/0aac9b091e8a1c001ab78acce07fa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Kaiser Permanente | [View](https://www.openjobs-ai.com/jobs/radiologic-technologist-lead-mammo-fresno-ca-127321025544192051) |
| AI Infrastructure Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/e6/9005dec1d704db70c308572cae0e6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> StackAI | [View](https://www.openjobs-ai.com/jobs/ai-infrastructure-engineer-san-francisco-ca-127321025544192052) |
| Mobile Design Engineer, iOS - React Native | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/1f/fd7c07d3cf727dfbec1ee327606fa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Slash | [View](https://www.openjobs-ai.com/jobs/mobile-design-engineer-ios-react-native-san-francisco-ca-127321025544192053) |
| OB/Gyn Physician in Escanaba, MI | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/e5/04c0d08b4d304d41b02b19eed8e62.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> OSF HealthCare | [View](https://www.openjobs-ai.com/jobs/obgyn-physician-in-escanaba-mi-escanaba-mi-127321025544192054) |
| US Tech - Salesforce Developer Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/us-tech-salesforce-developer-manager-cleveland-oh-127321025544192055) |
| RFM AI Governance Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/rfm-ai-governance-manager-cleveland-oh-127321025544192056) |
| Outside Sales Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/b7/6a3d1ba0926c4f0dec0135a107a0f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Shield Financial | [View](https://www.openjobs-ai.com/jobs/outside-sales-representative-winston-salem-nc-127321025544192057) |
| Tax Manager - Private Companies | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-manager-private-companies-nashville-tn-127321025544192058) |
| Asset & Wealth Management - Tax Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/asset-wealth-management-tax-senior-associate-detroit-mi-127321025544192059) |
| US Tech - Salesforce Developer Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/us-tech-salesforce-developer-manager-buffalo-ny-127321025544192060) |
| US Tech - Salesforce Developer Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/us-tech-salesforce-developer-manager-pittsburgh-pa-127321025544192061) |
| Microsoft D365 ERP (F&O) + AI/Copilot Functional Lead, Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/microsoft-d365-erp-fo-aicopilot-functional-lead-manager-san-antonio-tx-127321025544192062) |
| Microsoft D365 ERP (F&O) + AI/Copilot Functional Lead, Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/microsoft-d365-erp-fo-aicopilot-functional-lead-manager-richmond-va-127321025544192063) |
| Tax Director - Global Information Reporting | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-director-global-information-reporting-toledo-oh-127321025544192064) |
| Oracle EPM Consulting Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-epm-consulting-director-new-york-ny-127321025544192065) |
| Tax Senior Manager - Global Information Reporting | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-senior-manager-global-information-reporting-cincinnati-oh-127321025544192066) |
| NetSuite Integrations Consultant – Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/netsuite-integrations-consultant-manager-cincinnati-oh-127321025544192067) |
| Tax Manager - Personal Financial Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-manager-personal-financial-services-philadelphia-pa-127321025544192068) |
| UKG Pro WFM - Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/ukg-pro-wfm-senior-manager-florham-park-nj-127321025544192069) |
| AWS Engineer - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/aws-engineer-manager-phoenix-az-127321025544192070) |
| AWS Engineer - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/aws-engineer-manager-salt-lake-city-ut-127321025544192071) |
| Tax Senior Manager - Global Information Reporting | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-senior-manager-global-information-reporting-detroit-mi-127321025544192072) |
| Tax Director - Private Companies | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-director-private-companies-columbia-sc-127321025544192073) |
| UKG Pro WFM - Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/ukg-pro-wfm-senior-manager-salt-lake-city-ut-127321025544192074) |
| Managed Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SAP Functional Lead | [View](https://www.openjobs-ai.com/jobs/managed-services-sap-functional-lead-senior-associate-spartanburg-sc-127321025544192075) |
| AI First Software Engineer - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/ai-first-software-engineer-manager-chicago-il-127321025544192076) |
| Tax Manager - Personal Financial Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-manager-personal-financial-services-tampa-fl-127321025544192077) |
| Japanese Business Network - Private Tax Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/japanese-business-network-private-tax-manager-florham-park-nj-127321025544192078) |
| Partner Tax Preparation Advisor Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/partner-tax-preparation-advisor-senior-associate-oklahoma-city-ok-127321025544192079) |
| Oracle EPM Consulting Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-epm-consulting-director-washington-dc-127321025544192080) |
| Oracle HCM Cloud - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-hcm-cloud-manager-baltimore-md-127321025544192081) |
| Oracle EPM Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-epm-manager-dallas-tx-127321025544192082) |
| Digital Contact & Services Manager (AI & CCaaS) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/digital-contact-services-manager-ai-ccaas-denver-co-127321025544192083) |
| Google Cloud Architect - Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/google-cloud-architect-senior-manager-columbus-oh-127321025544192084) |
| Google Cloud Architect - Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/google-cloud-architect-senior-manager-nashville-tn-127321025544192085) |
| SAP Human Capital Payroll & Time Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/sap-human-capital-payroll-time-senior-manager-jacksonville-fl-127321025544192086) |
| Asset & Wealth Management Tax Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/asset-wealth-management-tax-manager-tulsa-ok-127321025544192087) |
| RFM AI Governance Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/rfm-ai-governance-manager-rochester-ny-127321025544192088) |
| SAP Human Capital Payroll & Time Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/sap-human-capital-payroll-time-senior-manager-miami-fl-127321025544192089) |
| Tax Manager - Private Companies | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-manager-private-companies-spartanburg-sc-127321025544192090) |
| Private Partnership Solutions (PPS) - Tax Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/private-partnership-solutions-pps-tax-senior-associate-silicon-valley-ca-127321025544192091) |
| Tax Director - Global Information Reporting | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-director-global-information-reporting-phoenix-az-127321025544192092) |
| Integration Architect – Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/integration-architect-director-detroit-mi-127321025544192093) |
| AWS Engineer - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/aws-engineer-manager-minneapolis-mn-127321025544192094) |
| Global Operations Lead, HCP Engagements - Managed Services Health PLS | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/global-operations-lead-hcp-engagements-managed-services-health-pls-indianapolis-in-127321025544192095) |
| Oracle HCM Cloud - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-hcm-cloud-manager-rosemont-il-127321025544192096) |
| Managed Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SAP Functional Lead | [View](https://www.openjobs-ai.com/jobs/managed-services-sap-functional-lead-senior-associate-little-rock-ar-127321025544192097) |
| Partner Tax Preparation Advisor Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/partner-tax-preparation-advisor-senior-associate-new-york-ny-127321025544192098) |
| Oracle CX Cloud Implementation Consultant - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-cx-cloud-implementation-consultant-manager-san-diego-ca-127321025544192099) |
| Tax Senior Manager - Private Companies | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-senior-manager-private-companies-atlanta-ga-127321025544192100) |
| Tax Senior Manager - Global Information Reporting | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-senior-manager-global-information-reporting-florham-park-nj-127321025544192101) |
| Hybrid Cloud & Tech Resilience - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/hybrid-cloud-tech-resilience-manager-silicon-valley-ca-127321025544192102) |
| NetSuite Integrations Consultant – Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/netsuite-integrations-consultant-manager-raleigh-nc-127321025544192103) |
| Asset & Wealth Management - Tax Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/asset-wealth-management-tax-senior-associate-silicon-valley-ca-127321025544192104) |
| Deals Diligence Analytics Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/deals-diligence-analytics-senior-associate-florham-park-nj-127321025544192105) |
| Tax Senior Manager - Global Information Reporting | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-senior-manager-global-information-reporting-houston-tx-127321025544192106) |
| Chinese Business Network - Private Tax Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/chinese-business-network-private-tax-manager-phoenix-az-127321025544192107) |
| Asset & Wealth Management - Renewable Energy Tax Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/asset-wealth-management-renewable-energy-tax-senior-manager-san-francisco-ca-127321025544192108) |
| Access Analytics, Ambulatory Operations Consultant, Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/access-analytics-ambulatory-operations-consultant-manager-nashville-tn-127321025544192109) |
| Microsoft D365 ERP (F&O) + AI/Copilot Functional Lead, Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/microsoft-d365-erp-fo-aicopilot-functional-lead-manager-buffalo-ny-127321025544192110) |
| Tax Senior Associate - Personal Financial Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-senior-associate-personal-financial-services-richmond-va-127321025544192111) |
| Oracle EPM Consulting Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-epm-consulting-director-chicago-il-127321025544192112) |
| Salesforce CPQ/Revenue Cloud Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/salesforce-cpqrevenue-cloud-director-pittsburgh-pa-127321025544192113) |
| Oracle CX Cloud Implementation Consultant - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-cx-cloud-implementation-consultant-manager-detroit-mi-127321025544192114) |
| UKG Pro WFM - Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/ukg-pro-wfm-senior-manager-des-moines-ia-127321025544192115) |
| Oracle HCM Cloud - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-hcm-cloud-manager-columbia-sc-127321025544192116) |
| Oracle HCM Cloud - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-hcm-cloud-manager-spartanburg-sc-127321025544192117) |
| Salesforce CPQ/Revenue Cloud Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/salesforce-cpqrevenue-cloud-director-las-vegas-nv-127321025544192118) |
| AI First Software Engineer - Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/ai-first-software-engineer-senior-associate-toledo-oh-127321025544192119) |
| Tax Director - Private Companies | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-director-private-companies-stamford-ct-127321025544192120) |
| Tax Senior Associate - Personal Financial Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-senior-associate-personal-financial-services-baltimore-md-127321025544192121) |
| Hybrid Cloud & Tech Resilience - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/hybrid-cloud-tech-resilience-manager-irvine-ca-127321025544192122) |
| Customs & International Trade Tax Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/customs-international-trade-tax-director-boston-ma-127321025544192123) |
| Tax Manager - Personal Financial Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-manager-personal-financial-services-austin-tx-127321025544192124) |
| Oracle CX Cloud Implementation Consultant - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-cx-cloud-implementation-consultant-manager-pittsburgh-pa-127321025544192125) |
| AI First Software Engineer - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/ai-first-software-engineer-manager-las-vegas-nv-127321025544192126) |
| Forward Deployed Software Engineer-Palantir Foundry-Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/forward-deployed-software-engineer-palantir-foundry-manager-irvine-ca-127321025544192127) |
| Managed Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> SAP Functional Lead | [View](https://www.openjobs-ai.com/jobs/managed-services-sap-functional-lead-senior-associate-tulsa-ok-127321025544192128) |
| Access Analytics, Ambulatory Operations Consultant, Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/access-analytics-ambulatory-operations-consultant-manager-columbus-oh-127321025544192129) |
| US Tech - Salesforce Developer Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/us-tech-salesforce-developer-manager-rochester-ny-127321025544192130) |
| Partner Tax Preparation Advisor Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/partner-tax-preparation-advisor-senior-associate-seattle-wa-127321025544192131) |
| Tax Senior Manager - Personal Financial Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-senior-manager-personal-financial-services-sacramento-ca-127321025544192132) |
| Oracle EPM Consulting Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-epm-consulting-director-montpelier-vt-127321025544192133) |
| AWS Engineer - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/aws-engineer-manager-san-antonio-tx-127321025544192134) |
| Chinese Business Network - Private Tax Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/chinese-business-network-private-tax-manager-grand-rapids-mi-127321025544192135) |
| Banking & Capital Markets Tax Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/banking-capital-markets-tax-director-silicon-valley-ca-127321025544192136) |
| Tax Senior Manager - Global Information Reporting | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-senior-manager-global-information-reporting-grand-rapids-mi-127321025544192137) |
| Oracle CX Cloud Implementation Consultant - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-cx-cloud-implementation-consultant-manager-milwaukee-wi-127321025544192138) |
| AWS Engineer - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/aws-engineer-manager-cleveland-oh-127321025544192139) |
| AI First Software Engineer - Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/ai-first-software-engineer-senior-associate-houston-tx-127321025544192140) |
| Financial Services Tax - Real Estate Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/financial-services-tax-real-estate-senior-manager-toledo-oh-127321025544192141) |
| Chinese Business Network - Private Tax Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/chinese-business-network-private-tax-manager-seattle-wa-127321025544192142) |
| Global Operations Lead, HCP Engagements - Managed Services Health PLS | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/global-operations-lead-hcp-engagements-managed-services-health-pls-buffalo-ny-127321025544192143) |
| Tax Director - Global Information Reporting | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-director-global-information-reporting-silicon-valley-ca-127321025544192144) |
| Private Partnership Solutions (PPS) - Tax Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/private-partnership-solutions-pps-tax-senior-manager-nashville-tn-127321025544192145) |
| Tax Senior Manager - Private Companies | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-senior-manager-private-companies-washington-dc-127321025544192146) |
| AWS Engineer - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/aws-engineer-manager-denver-co-127321025544192147) |
| Tax Manager - Private Companies | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-manager-private-companies-austin-tx-127321025544192148) |
| Hybrid Cloud & Tech Resilience - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/hybrid-cloud-tech-resilience-manager-florham-park-nj-127321025544192149) |
| Chinese Business Network - Private Tax Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/chinese-business-network-private-tax-manager-austin-tx-127321025544192150) |
| Tax Senior Manager - Global Information Reporting | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-senior-manager-global-information-reporting-spartanburg-sc-127321025544192151) |
| NetSuite Integrations Consultant – Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/netsuite-integrations-consultant-manager-philadelphia-pa-127321025544192152) |
| Access Analytics, Ambulatory Operations Consultant, Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/access-analytics-ambulatory-operations-consultant-manager-chicago-il-127321025544192153) |
| Google Cloud Architect - Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/google-cloud-architect-senior-manager-las-vegas-nv-127321025544192154) |
| SMT Operator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/1c/ec03ac0f6cb86f72bce1cc4b7e1f3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Celestica | [View](https://www.openjobs-ai.com/jobs/smt-operator-maple-grove-mn-127321025544192155) |
| Asset & Wealth Management Tax Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/asset-wealth-management-tax-manager-rosemont-il-127321025544192156) |
| Tax Senior Manager - Private Companies | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-senior-manager-private-companies-fort-worth-tx-127321025544192157) |
| Banking & Capital Markets Tax Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/banking-capital-markets-tax-manager-melville-ny-127321025544192158) |
| SAP Human Capital Payroll & Time Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/sap-human-capital-payroll-time-senior-manager-rosemont-il-127321025544192159) |
| SAP Human Capital Payroll & Time Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/sap-human-capital-payroll-time-senior-manager-birmingham-al-127321025544192160) |
| Tax Senior Manager - Global Information Reporting | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-senior-manager-global-information-reporting-st-louis-mo-127321025544192161) |
| Forward Deployed AI Engineer-Palantir Foundry-Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/forward-deployed-ai-engineer-palantir-foundry-senior-associate-san-antonio-tx-127321025544192162) |
| Forward Deployed Software Engineer-Palantir Foundry-Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/forward-deployed-software-engineer-palantir-foundry-manager-minneapolis-mn-127321025544192163) |
| Asset & Wealth Management - Renewable Energy Tax Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/asset-wealth-management-renewable-energy-tax-senior-manager-philadelphia-pa-127321025544192164) |
| Amada Senior Care - Caregivers Wanted | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/55/720756309c08a29fd9c0c75a394e8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Amada Senior Care Northshore | [View](https://www.openjobs-ai.com/jobs/amada-senior-care-caregivers-wanted-lake-bluff-il-127321025544192165) |
| Google Cloud Architect - Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/google-cloud-architect-senior-manager-albany-ny-127321025544192166) |
| Tax Manager - Personal Financial Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-manager-personal-financial-services-salt-lake-city-ut-127321025544192167) |
| Forward Deployed Software Engineer-Palantir Foundry-Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/forward-deployed-software-engineer-palantir-foundry-manager-houston-tx-127321025544192168) |
| Oracle CX Cloud Implementation Consultant - Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/oracle-cx-cloud-implementation-consultant-manager-stamford-ct-127321025544192169) |
| Asset & Wealth Management - Tax Senior Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/asset-wealth-management-tax-senior-associate-raleigh-nc-127321025544192170) |
| Asset & Wealth Management - Renewable Energy Tax Senior Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/asset-wealth-management-renewable-energy-tax-senior-manager-washington-dc-127321025544192171) |
| Tax Director - Private Companies | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/tax-director-private-companies-tampa-fl-127321025544192172) |
| Korean Business Network - Private Tax Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/e9/eb4f510fd5b7c1314d9f9b37e43f8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> PwC | [View](https://www.openjobs-ai.com/jobs/korean-business-network-private-tax-manager-birmingham-al-127321025544192173) |

<p align="center">
  <em>...and 549 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated January 23, 2026
</p>
