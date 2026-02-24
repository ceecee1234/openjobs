<p align="center">
  <img src="https://img.shields.io/badge/jobs-80+-blue?style=for-the-badge" alt="Jobs Count">
  <img src="https://img.shields.io/badge/companies-47+-purple?style=for-the-badge" alt="Companies">
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
- **Auto-Updated Every 6 Hours** - Fresh jobs from 47+ companies via GitHub Actions
- **Zero Infrastructure** - Runs entirely on GitHub Pages + Cloudflare (free tier)
- **Lightweight** - Pure Python, no external dependencies, <1MB total size
- **SEO Optimized** - Proper sitemaps, meta tags, and structured content

## Job Statistics

| Category | Count |
|----------|------:|
| Other | 53 |
| Healthcare | 8 |
| Engineering | 7 |
| Management | 5 |
| Sales | 4 |
| Finance | 2 |
| Marketing | 1 |
| HR | 0 |
| Operations | 0 |

**Top Hiring Companies:** Varsity Tutors, a Nerdy Company, One Medical, Allied Universal, Bentley Systems, Sevita

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
│  │ Sitemap     │   │ (80+ jobs) │   │ (README + HTML)     │   │
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
- **And 47+ other companies**

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
  <em>Updated February 24, 2026 · Showing 80 of 80+ jobs</em>
</p>

| Job Title | Company | Apply |
|-----------|---------|:-----:|
| Agricultural Science Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/agricultural-science-tutor-miami-fl-138541812154368026) |
| NCLEX-Registed Nurse Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/nclex-registed-nurse-tutor-detroit-mi-138541812154368027) |
| Macroeconomics Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/macroeconomics-tutor-memphis-tn-138541812154368028) |
| AP Microeconomics Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/ap-microeconomics-tutor-st-paul-mn-138541812154368029) |
| IB Chemistry Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/ib-chemistry-tutor-corpus-christi-tx-138541812154368030) |
| Microsoft Power BI Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/microsoft-power-bi-tutor-memphis-tn-138541812154368031) |
| Mandarin Chinese 2 Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/mandarin-chinese-2-tutor-st-paul-mn-138541812154368032) |
| Arabic Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/arabic-tutor-milwaukee-wi-138541812154368033) |
| Math 2 Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/math-2-tutor-corpus-christi-tx-138541812154368034) |
| AP English Literature and Composition Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/ap-english-literature-and-composition-tutor-henderson-nv-138541812154368035) |
| Piano Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/piano-tutor-boston-ma-138541812154368036) |
| General Chemistry 2 Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/general-chemistry-2-tutor-raleigh-nc-138541812154368037) |
| Grade 12 Chemistry Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/grade-12-chemistry-tutor-corpus-christi-tx-138541812154368038) |
| Senior Principal Software Engineer, Graphics | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/85/b881f928fe353efcb0cd03349def9.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Bentley Systems | [View](https://www.openjobs-ai.com/jobs/senior-principal-software-engineer-graphics-nevada-united-states-138541812154368039) |
| Real Estate License Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/real-estate-license-tutor-wichita-ks-138541812154368040) |
| Series 16 Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/series-16-tutor-henderson-nv-138541812154368041) |
| Arabic Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/arabic-tutor-louisville-ky-138541812154368042) |
| Caregiver | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/9d/79f0b46929b9fdcd3b849621cf917.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Sevita | [View](https://www.openjobs-ai.com/jobs/caregiver-williamsburg-ia-138541812154368043) |
| Senior Software Engineer, Backend - Distributed Systems | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/82/06b66a7fc28f284c531d77cfe6187.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Camunda | [View](https://www.openjobs-ai.com/jobs/senior-software-engineer-backend-distributed-systems-boston-ma-138541812154368044) |
| VOCATIONAL & LIFE SKILLS SPECIALIST | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/35/32e2d25c8f6de09f72ecd5e76b9d4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Catholic Charities of the Diocese of Rochester | [View](https://www.openjobs-ai.com/jobs/vocational-life-skills-specialist-rochester-ny-138541812154368045) |
| Housekeeper - Part Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/f0/a9ff7fcb3bfba67469e41830f505d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Three Oaks Assisted Living and Memory Care | [View](https://www.openjobs-ai.com/jobs/housekeeper-part-time-cary-il-138541812154368046) |
| RN Registered Nurse Pulse Cardiac Care Unit | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/5/fb/881bf3e57eb8b3449a49aacbd9a48.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MultiCare Health System | [View](https://www.openjobs-ai.com/jobs/rn-registered-nurse-pulse-cardiac-care-unit-puyallup-wa-138541812154368047) |
| Specialty Sales Representative - Pittsburgh South | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/2f/1ef9f03893dffedcbc37e662b91b5.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> ARS Pharmaceuticals, Inc. | [View](https://www.openjobs-ai.com/jobs/specialty-sales-representative-pittsburgh-south-united-states-138541812154368048) |
| Tax Partner | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/13/52313fb248ab49cef6bc66bc8fbaf.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Insite US | [View](https://www.openjobs-ai.com/jobs/tax-partner-jericho-ny-138541812154368049) |
| Jira & Confluence Setup - (Short Term Contract) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/50/20b5b03374228750835de379f2d1c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Anatta | [View](https://www.openjobs-ai.com/jobs/jira-confluence-setup-short-term-contract-charleston-sc-138541812154368050) |
| Primary Care Physician - Sign-On Bonus Available | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/d0/6cf69d842f10f4293de84194ba856.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> One Medical | [View](https://www.openjobs-ai.com/jobs/primary-care-physician-sign-on-bonus-available-berkeley-ca-138541812154368051) |
| Primary Care Physician - Sign-On Bonus Available | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/d0/6cf69d842f10f4293de84194ba856.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> One Medical | [View](https://www.openjobs-ai.com/jobs/primary-care-physician-sign-on-bonus-available-san-jose-ca-138541812154368052) |
| NeoCloud Senior Network Architect (Remote) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/9b/d3ba8cac0df971cb8c57b2e99a994.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Myriad360 | [View](https://www.openjobs-ai.com/jobs/neocloud-senior-network-architect-remote-new-york-ny-138541812154368053) |
| Quality Assurance Project Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/fe/665138d976099d40a5ceb7db4541b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Abbott | [View](https://www.openjobs-ai.com/jobs/quality-assurance-project-specialist-columbus-oh-138541812154368054) |
| Voice Engineer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/a/0b/d528988d43e228f1ddc521d8dd10f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Mastech Digital | [View](https://www.openjobs-ai.com/jobs/voice-engineer-arlington-va-138541812154368055) |
| Patient Meal Delivery Ambassador - Bluebonnet Full-Time | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/fd/17a54ae72b31cc4ee87ccdfded47f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Baton Rouge General Medical Center | [View](https://www.openjobs-ai.com/jobs/patient-meal-delivery-ambassador-bluebonnet-full-time-baton-rouge-la-138541812154368056) |
| Housekeeper | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/55/33b5ba78f65b5a20bde37238449f7.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Vi | [View](https://www.openjobs-ai.com/jobs/housekeeper-aventura-fl-138541812154368057) |
| Field Application Specialist- Filtration | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/0f/44f7fedba3f90774e45a5203c2491.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cytiva | [View](https://www.openjobs-ai.com/jobs/field-application-specialist-filtration-san-francisco-ca-138541812154368058) |
| Biochemistry Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/biochemistry-tutor-omaha-ne-138541812154368059) |
| College Economics Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/college-economics-tutor-kansas-city-mo-138541812154368060) |
| Vibe Coding Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/vibe-coding-tutor-albuquerque-nm-138541812154368061) |
| ARRT - Magnetic Resonance Imaging Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/arrt-magnetic-resonance-imaging-tutor-cleveland-oh-138541812154368062) |
| PANCE - Physician Assistant National Certifying Examination Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/pance-physician-assistant-national-certifying-examination-tutor-buffalo-ny-138541812154368063) |
| Probability Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/probability-tutor-fort-wayne-in-138541812154368064) |
| FTCE - Florida Teacher Certification Examinations Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/ftce-florida-teacher-certification-examinations-tutor-raleigh-nc-138541812154368065) |
| Structural Engineering Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/structural-engineering-tutor-st-paul-mn-138541812154368066) |
| LSAT Logical Reasoning Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/lsat-logical-reasoning-tutor-st-paul-mn-138541812154368067) |
| Portuguese Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/portuguese-tutor-louisville-ky-138541812154368068) |
| LSAT Logical Reasoning Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/lsat-logical-reasoning-tutor-new-orleans-la-138541812154368069) |
| Finance Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/finance-tutor-st-louis-mo-138541812154368070) |
| ISEE- Lower Level Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/isee-lower-level-tutor-kansas-city-mo-138541812154368071) |
| Biochemistry Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/biochemistry-tutor-pittsburgh-pa-138541812154368072) |
| College Biology Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/college-biology-tutor-new-orleans-la-138541812154368073) |
| Part-Time Radio Host/ Digital Content Writer - KHXT | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/7d/da19849c9f45acece0fb0c400075f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Townsquare Media | [View](https://www.openjobs-ai.com/jobs/part-time-radio-host-digital-content-writer-khxt-lafayette-la-138541812154368074) |
| High School Science Tutor | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/96/01490799486dac16a48801deb8255.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Varsity Tutors, a Nerdy Company | [View](https://www.openjobs-ai.com/jobs/high-school-science-tutor-henderson-nv-138541812154368075) |
| HOUSEKEEPER LEAD (FULL TIME) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/85/07fbb5811184a3ee8b4a837390e8e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Crothall Healthcare | [View](https://www.openjobs-ai.com/jobs/housekeeper-lead-full-time-albany-ga-138542072201216000) |
| Physician- Chief of Diagnostic Imaging Services | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/2d/6a84c07b0ab44c7a768e41821cb85.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> U.S. Department of Veterans Affairs | [View](https://www.openjobs-ai.com/jobs/physician-chief-of-diagnostic-imaging-services-spokane-wa-138542072201216001) |
| Security Guard - Unarmed Patrol Rounds | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f3/3df0322aff1b3ecad53afc60a98cb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Allied Universal | [View](https://www.openjobs-ai.com/jobs/security-guard-unarmed-patrol-rounds-atlanta-ga-138542072201216002) |
| In Process QA Associate | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/55/1e23aadfd21a1c776bec459fe46a2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Nivagen Pharmaceuticals, Inc. | [View](https://www.openjobs-ai.com/jobs/in-process-qa-associate-sacramento-ca-138542072201216003) |
| Security Shift Supervisor - Unarmed | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/f3/3df0322aff1b3ecad53afc60a98cb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Allied Universal | [View](https://www.openjobs-ai.com/jobs/security-shift-supervisor-unarmed-miami-fl-138542072201216004) |
| Lead Heavy Equipment Operator-Crew Leader | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/1/f1/28d7acf7664449464d7adfcc2b8be.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> York County, South Carolina | [View](https://www.openjobs-ai.com/jobs/lead-heavy-equipment-operator-crew-leader-york-sc-138542072201216005) |
| Manufacturing Engineer (Machining) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/d/1d/1faebca23841b08454d777591bf9f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Actalent | [View](https://www.openjobs-ai.com/jobs/manufacturing-engineer-machining-marengo-il-138542072201216006) |
| Cook | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/a3/0897471be93e650de2e0abffa0bbc.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Full Time | [View](https://www.openjobs-ai.com/jobs/cook-full-time-varies-flexible-hiram-ga-138542072201216008) |
| Helpdesk Support Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/30/b3e4070fe1c578187ad4643035517.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> TEKsystems | [View](https://www.openjobs-ai.com/jobs/helpdesk-support-technician-topeka-ks-138542072201216009) |
| Inbound Sales Representative | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/13/91f467628c89cab24860182f63f20.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Linxup | [View](https://www.openjobs-ai.com/jobs/inbound-sales-representative-chesterfield-mo-138542072201216011) |
| Treatment Plant Operator I - Surface Water | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/b3/752e9368239e092eac211c2b40127.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> City of Pearland, Texas | [View](https://www.openjobs-ai.com/jobs/treatment-plant-operator-i-surface-water-pearland-tx-138542072201216012) |
| Bioinformation B | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/a0/b7b8294e678b7a6abe1f8dc30f73e.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Inside Higher Ed | [View](https://www.openjobs-ai.com/jobs/bioinformation-b-philadelphia-pa-138542072201216013) |
| Accounting Generalist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/79/f31a67a67d7f322aa7b3807b0c788.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Aston Carter | [View](https://www.openjobs-ai.com/jobs/accounting-generalist-coeur-dalene-id-138542072201216014) |
| Key Account Specialist (Food Broker) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/d3/e864aca78ed84c7e4c512e64934fb.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Affinity Group, Sales & Marketing Agency | [View](https://www.openjobs-ai.com/jobs/key-account-specialist-food-broker-springfield-nj-138542072201216015) |
| Administrative Assistant - Bilingual | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/2e/463b502716a1887890b76bc0d53e3.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Catholic Funeral & Cemetery Services | [View](https://www.openjobs-ai.com/jobs/administrative-assistant-bilingual-antioch-ca-138542072201216016) |
| English Writing Generalist – Advanced | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/2c/fa2b73798467213ecb36f32690252.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Alignerr | [View](https://www.openjobs-ai.com/jobs/english-writing-generalist-advanced-dallas-tx-138542072201216018) |
| Software Application Developer | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/f/54/87a34e159f523a2f7886cfdae526a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Pinal County | [View](https://www.openjobs-ai.com/jobs/software-application-developer-florence-az-138542072201216019) |
| Secretary/Pacs Assistant - Evenings | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/b/3e/2d781abe8ce9b594c3c09f3e0405c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Smilow Cancer Hospital | [View](https://www.openjobs-ai.com/jobs/secretarypacs-assistant-evenings-new-london-ct-138542072201216020) |
| Teen Center Program Coordinator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/8/2a/45f937ae135dfc169b4747f8e3189.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Jubilee Housing | [View](https://www.openjobs-ai.com/jobs/teen-center-program-coordinator-washington-dc-138542072201216022) |
| Outside Sales Representative B2B | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/7/bb/bbd633a491a232123ecd11dc8f20b.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> CentiMark Corporation | [View](https://www.openjobs-ai.com/jobs/outside-sales-representative-b2b-fairfield-ca-138542072201216023) |
| Estimator | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/e/92/068d389a9ca279f4dc5f606cf881d.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> MGE Underground, Inc. | [View](https://www.openjobs-ai.com/jobs/estimator-fresno-ca-138542072201216024) |
| Veterinary Technician – GP/Urgent Care | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/c/ea/72f10fe0a0ea261c60716f44a2b62.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Papaya Veterinary Care | [View](https://www.openjobs-ai.com/jobs/veterinary-technician-gpurgent-care-san-diego-ca-138542072201216025) |
| Director of Information Security | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/3/b4/b1ecdbbf7029ecadeda95d167dbb2.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> RxVantage | [View](https://www.openjobs-ai.com/jobs/director-of-information-security-atlanta-ga-138542248361984000) |
| Configuration and Data Management Specialist | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/b4/0957d697429f60743c5a25e3bb385.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Amentum | [View](https://www.openjobs-ai.com/jobs/configuration-and-data-management-specialist-houston-tx-138542248361984001) |
| Telemetry Technician | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/2/06/0f89326449b64fedf1d825cd3db8f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Lifepoint Health® | [View](https://www.openjobs-ai.com/jobs/telemetry-technician-pasco-wa-138542248361984002) |
| Registered Nurse - York county | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/9/e7/31af770780c025217038292bc110f.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> AMEDISYS HOME HEALTH | [View](https://www.openjobs-ai.com/jobs/registered-nurse-york-county-lancaster-pa-138542248361984003) |
| CNC Machine Operator - Level 2 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/10/d0d0e80f6862256a963d5f1b79ca4.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Swagelok | [View](https://www.openjobs-ai.com/jobs/cnc-machine-operator-level-2-willoughby-oh-138542336442368000) |
| Licensed Practical Nurse (LPN) | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/6/ac/75acdf776653cac4fbf1ea8951160.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Cypress Skilled Nursing | [View](https://www.openjobs-ai.com/jobs/licensed-practical-nurse-lpn-cedartown-ga-138542336442368001) |
| Sales Design Consultant | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/0/8e/e3fa608d2d812b8c94f41207d464c.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Roche Bobois | [View](https://www.openjobs-ai.com/jobs/sales-design-consultant-pasadena-ca-138542336442368002) |
| KIP Summer 2026 | <img src="https://images.weserv.nl/?url=https://front.openjobs-ai.com/data/company-logo/v3/4/e6/4230cdc0eb5a620b7da9e2f87357a.png&w=24&h=24&q=80&output=webp" width="20" height="20" alt=""> Training and Education Intern | [View](https://www.openjobs-ai.com/jobs/kip-summer-2026-training-and-education-intern-atlas-network-arlington-va-138542336442368003) |

<p align="center">
  <em>...and 0 more jobs</em>
</p>

<p align="center">
  <a href="https://www.openjobs-ai.com/deepsearch"><strong>Browse All Jobs →</strong></a>
</p>

---

<p align="center">
  Made with Python + GitHub Actions · Updated February 24, 2026
</p>
