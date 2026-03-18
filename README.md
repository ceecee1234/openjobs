<p align="center">
  <img src="https://img.shields.io/badge/jobs-56+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-51+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 51+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 28 |
| Engineering | 11 |
| Healthcare | 11 |
| Management | 5 |
| Sales | 1 |
| Finance | 0 |
| Marketing | 0 |
| HR | 0 |
| Operations | 0 |

**Top Hiring Companies:** Broad River Rehab, Duke University Health System, BairesDev, Pacific Life, RRD

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
│  │ Sitemap     │   │ (56+ jobs) │   │ (README + HTML)     │   │
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
- **And 51+ other companies**

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
  <em>Updated March 18, 2026 · Showing 56 of 56+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| MIG Welder - ONeal Manufacturing Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/15/f3c9f6646a45981f1601d73e3bc84.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> O'Neal Steel | [View](https://www.openjobs-ai.com/jobs/mig-welder-oneal-manufacturing-services-houston-tx-146878633082880026) |
| PCA/HHA - Home Care Aide Position | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/5a/3ef605043edcc295370a9e3c15b40.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Crane Home Care, Inc. | [View](https://www.openjobs-ai.com/jobs/pcahha-home-care-aide-position-buffalo-ny-146878633082880027) |
| Physician Assistant in Clarion, PA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/7b/9462516890f0d087c6412ce463fe1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The IMA Group | [View](https://www.openjobs-ai.com/jobs/physician-assistant-in-clarion-pa-clarion-pa-146878633082880031) |
| Product Engineer II - FSC | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/f8/5bdbf3173c126db15806827ada278.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Parker Hannifin | [View](https://www.openjobs-ai.com/jobs/product-engineer-ii-fsc-otsego-mi-146878884741120000) |
| Freelance Data Annotator with Italian - AI Trainer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/41/2e99c9e67ab2e45d2966428c48e49.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Toloka Annotators | [View](https://www.openjobs-ai.com/jobs/freelance-data-annotator-with-italian-ai-trainer-texas-united-states-146878884741120001) |
| Sr Data Operations Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/53/adde0ed2a40feb1f56cc4a2852e28.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pacific Life | [View](https://www.openjobs-ai.com/jobs/sr-data-operations-engineer-omaha-ne-146878884741120002) |
| Sr Data Operations Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/53/adde0ed2a40feb1f56cc4a2852e28.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pacific Life | [View](https://www.openjobs-ai.com/jobs/sr-data-operations-engineer-newport-beach-ca-146878884741120003) |
| MRI Technologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/a6/e10e127898922fc0aa516d6b3449c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Talented Medical Solutions | [View](https://www.openjobs-ai.com/jobs/mri-technologist-shelton-ct-146878884741120004) |
| Head of External Communications | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/75/12206e45010f101a92d2ba18d24b5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Checkr, Inc. | [View](https://www.openjobs-ai.com/jobs/head-of-external-communications-san-francisco-ca-146878884741120005) |
| Medical Assistant -TMCOne - Knight Endocrinology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/2e/5197978ef00556a89426389272b53.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tucson Medical Center | [View](https://www.openjobs-ai.com/jobs/medical-assistant-tmcone-knight-endocrinology-tucson-az-146879006375936000) |
| Metals Equipment Technician - Nights | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/9f/b0391a244acb4be56ed4ec891ee7b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Samsung Semiconductor | [View](https://www.openjobs-ai.com/jobs/metals-equipment-technician-nights-austin-tx-146879006375936001) |
| Industrial Electrician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/2b/707b07d0fcf06d45c0dcbf014824a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Leggett & Platt | [View](https://www.openjobs-ai.com/jobs/industrial-electrician-conover-nc-146879006375936002) |
| Field Access Specialist - FAS | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f1/2a37454db659fd3ba867b9886a1fb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lundbeck | [View](https://www.openjobs-ai.com/jobs/field-access-specialist-fas-deerfield-il-146879006375936003) |
| Administrator - Fund Administration | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/f3/13645fdf06b3a9442fcd8eac7d59f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> JTC Group | [View](https://www.openjobs-ai.com/jobs/administrator-fund-administration-boston-ma-146879006375936004) |
| Evaluation Scenario Writer - AI Agent Testing Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/ec/51892dd947a93d01f1b95480b280c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mindrift | [View](https://www.openjobs-ai.com/jobs/evaluation-scenario-writer-ai-agent-testing-specialist-latin-america-146879144787968000) |
| Manufacturing Engineer - Littleton NH | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/786758f0a485ab0cfe57a82353557.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hubbell Incorporated | [View](https://www.openjobs-ai.com/jobs/manufacturing-engineer-littleton-nh-littleton-nh-146879224479744000) |
| Bindery Operator 1 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/64/4d4467d65cbcee2966f78aefadc37.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> RRD | [View](https://www.openjobs-ai.com/jobs/bindery-operator-1-orlando-fl-146878473699328045) |
| Senior Home Lending Advisor Eugene, OR | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/80/20f3cd27af58eca9c48426bfb1c4f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> JPMorganChase | [View](https://www.openjobs-ai.com/jobs/senior-home-lending-advisor-eugene-or-eugene-or-146878473699328046) |
| Clinical Nurse Leader - Emergency Department | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/86/5554267f8e683daeddb10b7337fd7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Duke University Health System | [View](https://www.openjobs-ai.com/jobs/clinical-nurse-leader-emergency-department-durham-nc-146878473699328047) |
| Medical Laboratory Technician - Riley Blood Bank | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/1f/82e49bae801110e99bcd57841853d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Indiana University Health | [View](https://www.openjobs-ai.com/jobs/medical-laboratory-technician-riley-blood-bank-indianapolis-in-146878473699328048) |
| QA Automation Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/96/576bb00bfe71e387d75356df83359.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Impiricus | [View](https://www.openjobs-ai.com/jobs/qa-automation-engineer-atlanta-ga-146878473699328049) |
| Sr. Software Engineer, Full Stack (C#.NET Core/GraphQL/API/React/Next.js) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/7b/a6621c260b225e06301b9b73047f6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Crum & Forster Services India Private Limited | [View](https://www.openjobs-ai.com/jobs/sr-software-engineer-full-stack-cnet-coregraphqlapireactnextjs-glastonbury-ct-146878473699328050) |
| LPN/RN ( PRN ) - LTC | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/cc/db1c9502e2b00991708a5d7ea2110.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Trinity Health Senior Communities | [View](https://www.openjobs-ai.com/jobs/lpnrn-prn-ltc-south-bend-in-146878473699328051) |
| Fire Systems Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/62/151b34270f1cc55088fb2af5b75a8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CaptiveAire Systems | [View](https://www.openjobs-ai.com/jobs/fire-systems-technician-columbia-sc-146878473699328052) |
| Product Demonstrator Part Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/5d/7affe96fe46d9e9d7d04b434f7be5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Product Connections | [View](https://www.openjobs-ai.com/jobs/product-demonstrator-part-time-wilkes-barre-pa-146878473699328053) |
| Receptionist - State Farm Agent Team Member | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/29/6642d139b1a83b74ad10b919847a7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> State Farm Agent | [View](https://www.openjobs-ai.com/jobs/receptionist-state-farm-agent-team-member-lincoln-ne-146878473699328054) |
| Mental Health Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/49/7829d7d7adf9e22f2d533b98f6361.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Valle del Sol | [View](https://www.openjobs-ai.com/jobs/mental-health-therapist-phoenix-az-146878473699328055) |
| Senior Staff Physical Design Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/71/d568efa18432c8d13441708920e4c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Marvell Technology | [View](https://www.openjobs-ai.com/jobs/senior-staff-physical-design-manager-santa-clara-ca-146878473699328056) |
| Occupational Therapy Assistant / COTA / OTA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/2e/bd059432654cc45638bd5e662a055.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Broad River Rehab | [View](https://www.openjobs-ai.com/jobs/occupational-therapy-assistant-cota-ota-darlington-sc-146878473699328057) |
| Occupational Therapy Assistant / COTA / OTA / PRN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/2e/bd059432654cc45638bd5e662a055.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Broad River Rehab | [View](https://www.openjobs-ai.com/jobs/occupational-therapy-assistant-cota-ota-prn-marion-oh-146878473699328058) |
| Physical Therapist / PT | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/2e/bd059432654cc45638bd5e662a055.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Broad River Rehab | [View](https://www.openjobs-ai.com/jobs/physical-therapist-pt-pawleys-island-sc-146878473699328059) |
| Postdoctoral Research Associate – AI in Nuclear Physics | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/1a/0525fb23633153c74c212d452d638.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Brookhaven National Laboratory | [View](https://www.openjobs-ai.com/jobs/postdoctoral-research-associate-ai-in-nuclear-physics-upton-ny-146878473699328062) |
| Lab Technician- Gene Transfer Center | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/b9/d38d0d470b0fe6b0e41496b4937a2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pillen Family Farms | [View](https://www.openjobs-ai.com/jobs/lab-technician-gene-transfer-center-columbus-ne-146878473699328063) |
| Mammography Technologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/d1/495a5c4550e7e002ce118dd9a197a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Akumin® | [View](https://www.openjobs-ai.com/jobs/mammography-technologist-plantation-fl-146878633082880000) |
| Software Platform Developer  (Hybrid) (Puerto Rico) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/42/f504ec7deb123193f731fd881fa4b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Collins Aerospace | [View](https://www.openjobs-ai.com/jobs/software-platform-developer-hybrid-puerto-rico-santa-isabel-co-146878633082880001) |
| Direct Support Professional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/cc/ca52bce9acdc7a17495369e4c4b29.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Merakey | [View](https://www.openjobs-ai.com/jobs/direct-support-professional-coraopolis-pa-146878633082880002) |
| Data Lake Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/3d/368c68fdf02a5f731733fb5a23764.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BairesDev | [View](https://www.openjobs-ai.com/jobs/data-lake-engineer-latin-america-146878633082880003) |
| HVAC Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/cb/0667cd4dcaa7cf23a020021cc6516.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Vaco by Highspring | [View](https://www.openjobs-ai.com/jobs/hvac-manager-maitland-fl-146878633082880004) |
| Enterprise Solution Architect | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/22/e4ca44b47b4b1428ed26ba2063d2c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Softensity Inc | [View](https://www.openjobs-ai.com/jobs/enterprise-solution-architect-latin-america-146878633082880005) |
| CT Technologist - Inpatient, Outpatient, & Interventional | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/86/5554267f8e683daeddb10b7337fd7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Duke University Health System | [View](https://www.openjobs-ai.com/jobs/ct-technologist-inpatient-outpatient-interventional-durham-nc-146878633082880007) |
| Talent Operations Manager - Remote Work | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/3d/368c68fdf02a5f731733fb5a23764.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> BairesDev | [View](https://www.openjobs-ai.com/jobs/talent-operations-manager-remote-work-latin-america-146878633082880009) |
| Customer Service Associate II | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/d7/0f1ab53210240fc6e6cc7b302bccf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bausch + Lomb | [View](https://www.openjobs-ai.com/jobs/customer-service-associate-ii-kirkwood-mo-146878633082880010) |
| Senior Strategy & Operations Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/b5/3bf9f547e81f02cb4429b881016fa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HTS Media (100% Remote | [View](https://www.openjobs-ai.com/jobs/senior-strategy-operations-manager-hts-media-100-remote-usa-austin-tx-146878633082880011) |
| News Associate Producer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/08/93e56058c7fd6513ea4220bdee5ed.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Fox Television Stations | [View](https://www.openjobs-ai.com/jobs/news-associate-producer-chicago-il-146878633082880012) |
| School Nurse (LPN or RN) Hempstead | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/5f/0bb2b3d7b93bb63bd6593e8b59630.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Gersh Autism Academy | [View](https://www.openjobs-ai.com/jobs/school-nurse-lpn-or-rn-hempstead-hempstead-ny-146878633082880013) |
| Assessor Supervisor - Lower Bucks | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/1a/a33cd351f232c273b22a23a5661cd.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Gaudenzia, Inc. | [View](https://www.openjobs-ai.com/jobs/assessor-supervisor-lower-bucks-bristol-pa-146878633082880014) |
| Engineering Manager, Liblab | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/8a/60ffb9659a84480d7905a90cec166.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Postman | [View](https://www.openjobs-ai.com/jobs/engineering-manager-liblab-austin-tx-146878633082880015) |
| Enterprise Account Executive - CO, KS, MO | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/35/adcca440539f12bea6366c3cf24e1.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Granicus | [View](https://www.openjobs-ai.com/jobs/enterprise-account-executive-co-ks-mo-united-states-146878633082880016) |
| Buyer - Sports Nutrition | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/5e/df9a35fccd82449d1debb6373b47c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> The Feed | [View](https://www.openjobs-ai.com/jobs/buyer-sports-nutrition-broomfield-co-146878633082880017) |
| Office Liaison | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/da/71522af928d3f303f8f48c7add0de.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Medical Center Health System | [View](https://www.openjobs-ai.com/jobs/office-liaison-odessa-tx-146878633082880018) |
| Maintenance Mechanic | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/22/0e5a829c6bcb9b4740d0e81f466da.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> IPG | [View](https://www.openjobs-ai.com/jobs/maintenance-mechanic-everetts-nc-146878633082880019) |
| MRI Tech Forsyth Outpatient (Weekend | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/2e/8943ac14e0fcaa78b967120320ec3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> 6:30a | [View](https://www.openjobs-ai.com/jobs/mri-tech-forsyth-outpatient-weekend-630a-7p-cumming-ga-146878633082880020) |
| Software Engineer (Engineer Software 2) - 26946 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/93/c9904b5532fd8bc32e6dddb65d2f2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> HII | [View](https://www.openjobs-ai.com/jobs/software-engineer-engineer-software-2-26946-suffolk-va-146878633082880021) |
| Janitor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f3/3df0322aff1b3ecad53afc60a98cb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Allied Universal | [View](https://www.openjobs-ai.com/jobs/janitor-dublin-ca-146878633082880023) |
| Occupational Therapist - The Healthcare Resort of Colorado Springs | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/63/e810709b6511371bef851ec16930f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Flagship Therapy | [View](https://www.openjobs-ai.com/jobs/occupational-therapist-the-healthcare-resort-of-colorado-springs-colorado-springs-co-146878633082880024) |
| Surgical Technologist / Night / SEIU - E I AGH | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/f8/cac30b742d64b4ec837083f80ce7b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Allegheny Health Network | [View](https://www.openjobs-ai.com/jobs/surgical-technologist-night-seiu-e-i-agh-pittsburgh-pa-146878633082880025) |

<p align="center">
  <em>...and 0 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated March 18, 2026
</p>
