<p align="center">
  <img src="https://img.shields.io/badge/jobs-951+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-563+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 563+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 428 |
| Healthcare | 218 |
| Engineering | 133 |
| Management | 112 |
| Finance | 22 |
| Sales | 17 |
| Marketing | 8 |
| Operations | 8 |
| HR | 5 |

**Top Hiring Companies:** DataAnnotation, Inside Higher Ed, UPMC, Jobot, Deloitte

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
│  │ Sitemap     │   │ (951+ jobs) │   │ (README + HTML)     │   │
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
- **And 563+ other companies**

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
  <em>Updated February 06, 2026 · Showing 200 of 951+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Radiation Therapist - Per Diem | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/43/4537f1d19c39f958a4e46f8c3491c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UVM Health | [View](https://www.openjobs-ai.com/jobs/radiation-therapist-per-diem-burlington-vt-132385152696320057) |
| Personal Injury Attorney- (Bilingual Spanish) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a3/925240adc00ae615c5d8e4a93218d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Alexandra Lozano Immigration Law PLLC | [View](https://www.openjobs-ai.com/jobs/personal-injury-attorney-bilingual-spanish-seattle-wa-132385152696320058) |
| Scientist 1 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/5c/a679e34bbcc5ea09978a4a9f89569.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pace® Labs | [View](https://www.openjobs-ai.com/jobs/scientist-1-bakersfield-ca-132385152696320059) |
| Per Diem Radiology Opportunities: X-ray, CT, MRI, Mammography, and Ultrasound | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/43/4537f1d19c39f958a4e46f8c3491c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UVM Health | [View](https://www.openjobs-ai.com/jobs/per-diem-radiology-opportunities-x-ray-ct-mri-mammography-and-ultrasound-burlington-vt-132385152696320060) |
| Audiologist - Part Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/43/4537f1d19c39f958a4e46f8c3491c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UVM Health | [View](https://www.openjobs-ai.com/jobs/audiologist-part-time-burlington-vt-132385152696320061) |
| Sonographer II Mon-Fri Days (New Langhorne Location) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/92/1be8c595d57c7bc8da0dc0b667962.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Centra Health | [View](https://www.openjobs-ai.com/jobs/sonographer-ii-mon-fri-days-new-langhorne-location-lynchburg-va-132385152696320062) |
| Sr. Director - API Manufacturing Quality Control | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/fb/8466bd490fe0fbf86e4b2a0140416.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Eli Lilly and Company | [View](https://www.openjobs-ai.com/jobs/sr-director-api-manufacturing-quality-control-houston-tx-132385152696320063) |
| Estate & Trust Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/1f/c773b5cfcb2a0563431883681f25d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Navolio & Tallman LLP | [View](https://www.openjobs-ai.com/jobs/estate-trust-manager-walnut-creek-ca-132385152696320064) |
| Senior Analyst, Security Operations | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/1b/19461ba6d09181341e13486e3bece.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Symbotic | [View](https://www.openjobs-ai.com/jobs/senior-analyst-security-operations-wilmington-ma-132385152696320065) |
| Multimodality Radiologic Tech (Per Diem) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/2c/ac00117d72fdd99aa6ae922e032b3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UVM Health | [View](https://www.openjobs-ai.com/jobs/multimodality-radiologic-tech-per-diem-middlebury-vt-132385152696320066) |
| PRN Home Health OT | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/99/0a51719800d760f77ff0e2a915337.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inspired HomeCare | [View](https://www.openjobs-ai.com/jobs/prn-home-health-ot-plano-il-132385152696320067) |
| Mental Health Technician - Emergency Department | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/43/4537f1d19c39f958a4e46f8c3491c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UVM Health | [View](https://www.openjobs-ai.com/jobs/mental-health-technician-emergency-department-burlington-vt-132385152696320068) |
| Senior Projects Mgr, PDC | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/3b/05369d206e99008bf7f2769a0dee6.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> UW Health SwedishAmerican | [View](https://www.openjobs-ai.com/jobs/senior-projects-mgr-pdc-rockford-il-132385152696320069) |
| Telemetry RN | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/fd/87e099ca4630b42393bb3f9f936c9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Trinity Health | [View](https://www.openjobs-ai.com/jobs/telemetry-rn-boise-id-132385152696320070) |
| Analyst, Personal Property Tax | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/0c/7ccc7a4f0aff03c915c485565b9da.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ryan | [View](https://www.openjobs-ai.com/jobs/analyst-personal-property-tax-scottsdale-az-132385152696320071) |
| Metrology Technician, Megafactory | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/0b/90ccf85fb6d59c02cf47ec36866aa.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Tesla | [View](https://www.openjobs-ai.com/jobs/metrology-technician-megafactory-brookshire-tx-132385152696320072) |
| R&D Senior Tax Manager, Federal Tax Consulting Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/34/baecfd5da0cd9d133c82c10c41a0d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Crowe | [View](https://www.openjobs-ai.com/jobs/rd-senior-tax-manager-federal-tax-consulting-services-atlanta-ga-132385152696320073) |
| Senior Client Executive-Automotive (US-Detroit) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/dd/2f5da4e1701ae0a7b0f02d77c5b72.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> NTT DATA North America | [View](https://www.openjobs-ai.com/jobs/senior-client-executive-automotive-us-detroit-detroit-mi-132385152696320074) |
| RF Antenna AESA Design Engineer, Principal- Various Locations Pipeline | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/00/9441f427f26d04f8d6583d2ec74ea.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lockheed Martin | [View](https://www.openjobs-ai.com/jobs/rf-antenna-aesa-design-engineer-principal-various-locations-pipeline-grand-prairie-tx-132385152696320075) |
| Sr. Security Solutions Engineer (Zero Trust & Cloud Security) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/a3/101d8e97a43ec4d33bd575e343998.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Active Cyber | [View](https://www.openjobs-ai.com/jobs/sr-security-solutions-engineer-zero-trust-cloud-security-united-states-132385152696320076) |
| Senior Revenue Financial Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/98/ea32b23bc8f90c8e9047bb1632c9a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Aegis Sciences Corporation | [View](https://www.openjobs-ai.com/jobs/senior-revenue-financial-analyst-nashville-tn-132385152696320077) |
| Assistant Project Manager, NA | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/6a/7e600f335f47254847dfb45832ac5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Vantage Data Centers | [View](https://www.openjobs-ai.com/jobs/assistant-project-manager-na-santa-clara-ca-132385152696320078) |
| Neurologist - Movement Disorder Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/fb/0d2aa9825dac69ec4cbd0638668a9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Hackensack Meridian Health | [View](https://www.openjobs-ai.com/jobs/neurologist-movement-disorder-specialist-hackensack-nj-132385152696320079) |
| Frontend Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/frontend-developer-rhode-island-united-states-132385152696320080) |
| Account Director | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/7a/9ae9c98e994e8ea6080c453305fe8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cheil USA | [View](https://www.openjobs-ai.com/jobs/account-director-plano-tx-132385152696320081) |
| Senior Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/f8/5bdbf3173c126db15806827ada278.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Parker Hannifin | [View](https://www.openjobs-ai.com/jobs/senior-engineer-greensboro-nc-132385152696320082) |
| AI Content Writer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/ai-content-writer-massachusetts-united-states-132385152696320083) |
| Cardiac Sonographer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/cardiac-sonographer-missouri-united-states-132385152696320084) |
| Frontend Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/frontend-developer-missouri-united-states-132385152696320085) |
| Graduate Research Intern, Chemistry | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/graduate-research-intern-chemistry-california-united-states-132385152696320086) |
| Mathematics Education Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/mathematics-education-specialist-wisconsin-united-states-132385152696320087) |
| Interpreter | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/interpreter-kentucky-united-states-132385152696320088) |
| Graduate Research Intern, Chemistry | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/graduate-research-intern-chemistry-rhode-island-united-states-132385152696320089) |
| Physics Instructor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/physics-instructor-oregon-united-states-132385152696320090) |
| Physics Teacher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/physics-teacher-new-york-united-states-132385152696320091) |
| Retail Customer Service Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/retail-customer-service-associate-alaska-united-states-132385152696320092) |
| Game Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/game-developer-montana-united-states-132385152696320093) |
| Postdoctoral Math Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/postdoctoral-math-associate-oklahoma-united-states-132385152696320094) |
| Data Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/data-engineer-idaho-united-states-132385152696320095) |
| Graduate Research Intern, Chemistry | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/graduate-research-intern-chemistry-arkansas-united-states-132385152696320096) |
| Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/nurse-mississippi-united-states-132385152696320097) |
| Content Developer (Mathematics) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/content-developer-mathematics-north-dakota-united-states-132385152696320098) |
| Financial Planner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/financial-planner-montana-united-states-132385152696320099) |
| AI Trainer - Chemistry | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/ai-trainer-chemistry-delaware-united-states-132385152696320100) |
| Physics Teacher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/physics-teacher-rhode-island-united-states-132385152696320101) |
| Family Medicine Physician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/family-medicine-physician-illinois-united-states-132385152696320102) |
| Math Teacher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/math-teacher-vermont-united-states-132385152696320103) |
| Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/nurse-montana-united-states-132385152696320104) |
| Full Stack Developer (UX/UI) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/full-stack-developer-uxui-new-york-united-states-132385152696320105) |
| Securities Lawyer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/securities-lawyer-wyoming-united-states-132385152696320106) |
| Physics Research Scientist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/physics-research-scientist-mississippi-united-states-132385152696320107) |
| Data Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/data-engineer-tennessee-united-states-132385152696320108) |
| Frontend Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/frontend-developer-utah-united-states-132385152696320109) |
| Content Developer (Mathematics) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/content-developer-mathematics-wisconsin-united-states-132385152696320110) |
| Math Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/math-tutor-new-jersey-united-states-132385152696320111) |
| Retail Customer Service Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/retail-customer-service-associate-kentucky-united-states-132385152696320112) |
| Quantitative Researcher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/quantitative-researcher-south-carolina-united-states-132385152696320113) |
| Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/tutor-hawaii-united-states-132385152696320114) |
| Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/tutor-oregon-united-states-132385152696320115) |
| Bilingual Customer Support Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/bilingual-customer-support-specialist-arkansas-united-states-132385152696320116) |
| Bilingual Customer Support Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/bilingual-customer-support-specialist-texas-united-states-132385152696320117) |
| Mathematics Education Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/mathematics-education-specialist-arizona-united-states-132385152696320118) |
| Physics Research Scientist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/physics-research-scientist-massachusetts-united-states-132385152696320119) |
| Math Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/math-tutor-connecticut-united-states-132385152696320120) |
| Financial Planner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/financial-planner-utah-united-states-132385152696320121) |
| Math Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/math-tutor-south-dakota-united-states-132385152696320122) |
| Massage Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/massage-therapist-minnesota-united-states-132385152696320123) |
| UI Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/ui-developer-vermont-united-states-132385152696320124) |
| Graduate Research Intern, Chemistry | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/graduate-research-intern-chemistry-oregon-united-states-132385152696320125) |
| Receptionist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/receptionist-indiana-united-states-132385152696320126) |
| Digital Marketer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/digital-marketer-illinois-united-states-132385152696320127) |
| Chemistry Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/chemistry-tutor-florida-united-states-132385152696320128) |
| Interpreter | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/interpreter-iowa-united-states-132385152696320129) |
| Content Developer - Biology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/content-developer-biology-nevada-united-states-132385152696320130) |
| Full Stack Developer (UX/UI) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/full-stack-developer-uxui-pennsylvania-united-states-132385152696320131) |
| Pediatrician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/pediatrician-north-dakota-united-states-132385152696320132) |
| Clinical Laboratory Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/clinical-laboratory-technician-north-carolina-united-states-132385152696320133) |
| Interpreter | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/interpreter-idaho-united-states-132385152696320134) |
| International Lawyer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/international-lawyer-missouri-united-states-132385152696320135) |
| Hospice Aide (CNA) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/a3/81bda4ccdd53342867f57c9196608.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> A HUG AWAY, INC | [View](https://www.openjobs-ai.com/jobs/hospice-aide-cna-katy-tx-132385152696320136) |
| Game Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/game-developer-alabama-united-states-132385152696320137) |
| Physics Research Scientist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/physics-research-scientist-alabama-united-states-132385152696320138) |
| Front End Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/front-end-engineer-michigan-united-states-132385152696320139) |
| Front End Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/front-end-engineer-tennessee-united-states-132385152696320140) |
| AI Trainer - Chemistry | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/ai-trainer-chemistry-alaska-united-states-132385152696320141) |
| MRI Technologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/mri-technologist-tennessee-united-states-132385152696320142) |
| Chemistry Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/chemistry-tutor-minnesota-united-states-132385152696320143) |
| Phlebotomist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/phlebotomist-florida-united-states-132385152696320144) |
| Tax Attorney | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/tax-attorney-colorado-united-states-132385152696320145) |
| Chemistry Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/chemistry-tutor-pennsylvania-united-states-132385152696320146) |
| Postdoctoral Chemistry Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/postdoctoral-chemistry-associate-maryland-united-states-132385152696320147) |
| Real Estate Attorney | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/real-estate-attorney-iowa-united-states-132385152696320148) |
| Swift Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/swift-developer-washington-dc-132385152696320149) |
| AI Content Writer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/ai-content-writer-california-united-states-132385152696320150) |
| Data Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/data-engineer-south-dakota-united-states-132385152696320151) |
| AI Trainer - Chemistry | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/ai-trainer-chemistry-georgia-united-states-132385152696320152) |
| Graduate Research Intern, Chemistry | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/graduate-research-intern-chemistry-oklahoma-united-states-132385152696320153) |
| Full Stack Developer (UX/UI) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/full-stack-developer-uxui-utah-united-states-132385152696320154) |
| Chemical Engineer - AI Trainer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/chemical-engineer-ai-trainer-indiana-united-states-132385152696320155) |
| Chemistry Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/chemistry-tutor-north-dakota-united-states-132385152696320156) |
| Clinical Reviewer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/clinical-reviewer-nebraska-united-states-132385152696320157) |
| Copyright Attorney | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/copyright-attorney-colorado-united-states-132385152696320158) |
| AI Training, Mathematics | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/ai-training-mathematics-massachusetts-united-states-132385152696320159) |
| Swift Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/swift-developer-nevada-united-states-132385152696320160) |
| Data Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/data-engineer-vermont-united-states-132385152696320161) |
| AI Content Writer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/ai-content-writer-wyoming-united-states-132385152696320162) |
| AI Trainer - Chemistry | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/ai-trainer-chemistry-new-york-united-states-132385152696320164) |
| Constitutional Lawyer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/constitutional-lawyer-iowa-united-states-132385152696320165) |
| Retail Customer Service Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/retail-customer-service-associate-south-carolina-united-states-132385152696320166) |
| Physical Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/physical-therapist-pennsylvania-united-states-132385152696320167) |
| Compliance Attorney | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/compliance-attorney-alaska-united-states-132385152696320168) |
| Systems Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/systems-developer-pennsylvania-united-states-132385152696320169) |
| Real Estate Attorney | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/real-estate-attorney-texas-united-states-132385152696320170) |
| AI Training Chemistry | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/ai-training-chemistry-georgia-united-states-132385152696320171) |
| Content Developer (Mathematics) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/content-developer-mathematics-connecticut-united-states-132385152696320172) |
| Math Teacher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/math-teacher-florida-united-states-132385152696320173) |
| Content Developer (Physics) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/content-developer-physics-tennessee-united-states-132385152696320174) |
| Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/tutor-north-dakota-united-states-132385152696320175) |
| Family Medicine Physician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/family-medicine-physician-vermont-united-states-132385152696320176) |
| Receptionist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/receptionist-arizona-united-states-132385152696320177) |
| Biology Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/biology-tutor-ohio-united-states-132385152696320178) |
| Marketing Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/marketing-coordinator-louisiana-united-states-132385152696320179) |
| Prompt Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/prompt-engineer-ohio-united-states-132385152696320180) |
| Cardiologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/cardiologist-south-dakota-united-states-132385152696320181) |
| Criminal Defense Attorney | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/criminal-defense-attorney-idaho-united-states-132385152696320182) |
| Swift Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/swift-developer-rhode-island-united-states-132385152696320183) |
| Swift Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/swift-developer-washington-united-states-132385152696320184) |
| AI Content Writer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/ai-content-writer-tennessee-united-states-132385152696320185) |
| Mathematics Education Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/mathematics-education-specialist-louisiana-united-states-132385152696320186) |
| Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/nurse-hawaii-united-states-132385152696320187) |
| Teacher Of Chemistry | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/teacher-of-chemistry-tennessee-united-states-132385152696320188) |
| Clinical Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/clinical-specialist-rhode-island-united-states-132385152696320189) |
| Constitutional Lawyer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/constitutional-lawyer-idaho-united-states-132385152696320190) |
| Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/tutor-michigan-united-states-132385152696320191) |
| Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/tutor-montana-united-states-132385152696320192) |
| Purchasing Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/purchasing-specialist-north-dakota-united-states-132385152696320193) |
| Purchasing Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/purchasing-specialist-arizona-united-states-132385152696320194) |
| Full Stack Developer (UX/UI) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/full-stack-developer-uxui-montana-united-states-132385152696320195) |
| Chemical Engineer - AI Trainer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/chemical-engineer-ai-trainer-arkansas-united-states-132385152696320196) |
| Content Developer (Chemistry) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/content-developer-chemistry-wisconsin-united-states-132385152696320197) |
| Chemical Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/chemical-engineer-new-york-united-states-132385152696320198) |
| Internal Medicine Physician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/internal-medicine-physician-kansas-united-states-132385152696320199) |
| Tax Attorney | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/tax-attorney-indiana-united-states-132385152696320200) |
| Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/analyst-north-carolina-united-states-132385152696320201) |
| Software Designer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/software-designer-alabama-united-states-132385152696320202) |
| AI Training, Mathematics | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/ai-training-mathematics-california-united-states-132385152696320203) |
| Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/analyst-arizona-united-states-132385152696320204) |
| Data Scientist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/data-scientist-montana-united-states-132385152696320205) |
| Cardiologist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/cardiologist-nebraska-united-states-132385152696320206) |
| Corporate Attorney | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/corporate-attorney-washington-dc-132385152696320207) |
| Process Development Chemist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/process-development-chemist-missouri-united-states-132385152696320208) |
| Process Development Chemist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/process-development-chemist-new-mexico-united-states-132385152696320209) |
| Postdoctoral Researcher (Chemistry) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/postdoctoral-researcher-chemistry-kansas-united-states-132385152696320210) |
| Finance Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/finance-associate-south-dakota-united-states-132385152696320211) |
| Full Stack Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/full-stack-engineer-north-dakota-united-states-132385152696320212) |
| Postdoctoral Math Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/postdoctoral-math-associate-montana-united-states-132385152696320213) |
| Digital Marketer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/digital-marketer-massachusetts-united-states-132385152696320214) |
| AI Content Writer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/ai-content-writer-colorado-united-states-132385152696320215) |
| Teacher of Mathematics | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/teacher-of-mathematics-idaho-united-states-132385152696320216) |
| Math Teacher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/math-teacher-washington-dc-132385152696320217) |
| Phlebotomist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/phlebotomist-new-jersey-united-states-132385152696320218) |
| Phlebotomist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/phlebotomist-washington-united-states-132385152696320219) |
| Massage Therapist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/massage-therapist-nebraska-united-states-132385152696320220) |
| Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/analyst-arkansas-united-states-132385152696320221) |
| Teacher of Biology | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/teacher-of-biology-arkansas-united-states-132385152696320222) |
| Event Planner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/event-planner-new-jersey-united-states-132385152696320223) |
| Analyst | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/analyst-washington-dc-132385152696320224) |
| Human Rights Lawyer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/human-rights-lawyer-michigan-united-states-132385152696320225) |
| Legal Writer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/legal-writer-louisiana-united-states-132385152696320226) |
| Pharmacy Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/pharmacy-technician-idaho-united-states-132385152696320227) |
| Software Designer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/software-designer-north-carolina-united-states-132385152696320228) |
| Research And Development Mathematician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/research-and-development-mathematician-washington-united-states-132385152696320229) |
| Customer Support Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/customer-support-specialist-vermont-united-states-132385152696320230) |
| Primary Teacher | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/primary-teacher-new-jersey-united-states-132385152696320231) |
| Cardiac Sonographer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/cardiac-sonographer-new-york-united-states-132385152696320232) |
| Front End Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/front-end-engineer-nebraska-united-states-132385152696320233) |
| Mathematics Education Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/mathematics-education-specialist-maryland-united-states-132385152696320234) |
| Graduate Research Intern, Chemistry | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/graduate-research-intern-chemistry-alabama-united-states-132385152696320235) |
| Clinical Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/clinical-specialist-utah-united-states-132385152696320236) |
| Event Planner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/event-planner-louisiana-united-states-132385152696320237) |
| Event Planner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/event-planner-delaware-united-states-132385152696320238) |
| Dietitian | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0d/3bd281d85767cab08e7d6c379188d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> DataAnnotation | [View](https://www.openjobs-ai.com/jobs/dietitian-maryland-united-states-132385152696320239) |
| RN Outpatient | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/a4/ebab54a580dbfc71fdd4c5b098ecb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MRI | [View](https://www.openjobs-ai.com/jobs/rn-outpatient-mri-prn-1st-shift-huntsville-al-132385794424832000) |
| Medical Transport | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/9d/79f0b46929b9fdcd3b849621cf917.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sevita | [View](https://www.openjobs-ai.com/jobs/medical-transport-denton-tx-132385794424832001) |
| Back End Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/53/470ba023229f5441cebe78b8a57df.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Ruvixx, Inc. | [View](https://www.openjobs-ai.com/jobs/back-end-developer-latin-america-132385794424832002) |
| Senior Client Solutions Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/4a/72618bacd37551f80d8bc1fb95451.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AHEAD | [View](https://www.openjobs-ai.com/jobs/senior-client-solutions-engineer-san-diego-ca-132385794424832003) |
| Manual QA (Front End & Salesforce) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/66/97d7f8bb82e4c85ea4c7abf0aa759.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Perform | [View](https://www.openjobs-ai.com/jobs/manual-qa-front-end-salesforce-latin-america-132385794424832004) |
| Eastern Great Lakes Sales Territory Manager | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/5b/fa389abc1e47938f85e2748d83aec.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Rainbow Ecoscience | [View](https://www.openjobs-ai.com/jobs/eastern-great-lakes-sales-territory-manager-michigan-united-states-132385794424832005) |
| Accounting Manager – Cost Accounting/Controlling | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/40/2eecd32fa803437dc5757674d6236.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Olin | [View](https://www.openjobs-ai.com/jobs/accounting-manager-cost-accountingcontrolling-houston-tx-132385794424832006) |
| Administrative Assistant - Traverse City, MI | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/d0/0d1aa4fd61fbcef20f2c7a9a99091.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Plante Moran | [View](https://www.openjobs-ai.com/jobs/administrative-assistant-traverse-city-mi-traverse-city-mi-132385794424832007) |
| Senior Electrical & Control Designer 2 - Government Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/92/63e48b92ca6f1137597aecd99edf7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sargent & Lundy | [View](https://www.openjobs-ai.com/jobs/senior-electrical-control-designer-2-government-services-richland-wa-132385794424832008) |
| Channel Marketer, Associate - Blackstone Private Wealth | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/f4/67c11e33d14af61a63441fd5c8e9f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Blackstone | [View](https://www.openjobs-ai.com/jobs/channel-marketer-associate-blackstone-private-wealth-new-york-ny-132385794424832009) |
| Senior Systems Administrator (Systems Administrator 3) - 25202 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/ca/87ab537107e2cf356ab94d5f6daf0.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mission Technologies, a division of HII | [View](https://www.openjobs-ai.com/jobs/senior-systems-administrator-systems-administrator-3-25202-hanover-md-132385794424832010) |
| Senior Applications Support Analyst - Assistant Vice President | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/28/f83c90ef9f50c06d88cf660f9eca9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Citi | [View](https://www.openjobs-ai.com/jobs/senior-applications-support-analyst-assistant-vice-president-tampa-fl-132385794424832011) |
| Laser Machine Assembler | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/83/55b0197352386eb045f1dbd259dc8.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> TRUMPF North America | [View](https://www.openjobs-ai.com/jobs/laser-machine-assembler-farmington-ct-132385794424832012) |
| PD Cat Scan Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/60/bb06d755e432ab938eb6d36ce0206.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> RWJBarnabas Health | [View](https://www.openjobs-ai.com/jobs/pd-cat-scan-technician-elizabeth-nj-132385794424832013) |
| Registered Nurse | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/de/e6d2da9922c3ff6396c112d92c457.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Float Pool | [View](https://www.openjobs-ai.com/jobs/registered-nurse-float-pool-critical-care-cincinnati-oh-132385794424832014) |
| Funding Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/7c/c77e4d8d482e1b4e71113d9c3a511.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Union Home Mortgage Corp. | [View](https://www.openjobs-ai.com/jobs/funding-specialist-strongsville-oh-132385794424832015) |
| Director of Operations - PE Backed | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/d4/cbf18a881a8401072a728b9fa8e7c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Aviva Aesthetics | [View](https://www.openjobs-ai.com/jobs/director-of-operations-pe-backed-united-states-132385794424832016) |
| Extraction Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/8b/61266fb4599a15605e50ccd104039.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Verano | [View](https://www.openjobs-ai.com/jobs/extraction-specialist-somerville-nj-132385794424832017) |

<p align="center">
  <em>...and 751 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated February 06, 2026
</p>
