# AI Cyber Hygiene Awareness Campaign for Students

**Capstone 15 | Prepared by Nithyasri**  
**Audience:** Students aged 15–24, including non-technical learners  
**Campaign focus:** Software updates, backups, app permissions, public Wi-Fi and safe browsing

## Project overview
This project develops and evaluates an AI-assisted cyber-hygiene awareness campaign. AI is used to support research synthesis, drafting, repurposing content and a small repeatable content workflow. Safety-critical claims are checked against authoritative guidance before publication.

## Campaign objectives
1. Explain five everyday cyber-hygiene behaviours in accessible language.
2. Produce reusable educational content across text, social, presentation and video formats.
3. Document prompt design, source verification, error analysis and responsible AI use.
4. Provide a simple local automation that converts approved campaign tips into draft social copy.
5. Compare an initial AI draft with a source-checked, human-edited version.

## Deliverables
| Deliverable | Location |
|---|---|
| Research report | `research/research-report.md` |
| Awareness article | `content/awareness-article.md` |
| Six social posts | `content/social-media-posts.md` |
| Video script and storyboard | `content/video-script-storyboard.md` |
| Ten-question quiz and key | `content/quiz.md` |
| Tip dataset and generator | `automation/` |
| Prompt library | `documentation/prompt-library.md` |
| Verification and error analysis | `documentation/verification-and-error-analysis.md` |
| Before/after comparison | `documentation/before-after-analysis.md` |
| Responsible AI notes | `documentation/responsible-ai-and-limitations.md` |
| AI tools and skills register | `documentation/ai-tools-and-skills-register.md` |
| Live demo guide | `documentation/demo-guide.md` |
| Presentation | [Editable Canva presentation](https://canva.link/sb154mzu9jjjh18) |

## Use and verification
This repository is an educational prototype. Do not treat campaign copy as incident-response or organisation-specific security advice. Review official guidance and local policies before reuse. The verification log distinguishes checked claims from claims that still require a recorded manual review.

## Run the automation
Requires Python 3.10+; no third-party packages are required.

```bash
python automation/generate_tip_drafts.py
```

The script reads `automation/tips.csv` and writes `automation/generated_posts.md`. Review every generated draft before publishing.

## Repository structure
```
.
├── README.md
├── research/
├── content/
├── automation/
└── documentation/
```

## Primary reference sources
- CERT-In: https://www.cert-in.org.in/
- CISA Secure Our World: https://www.cisa.gov/secure-our-world
- FTC: https://consumer.ftc.gov/articles/how-use-public-wi-fi-networks
- Google Android Help — app permissions: https://support.google.com/android/answer/9431959
- Microsoft Support — back up and restore: https://support.microsoft.com/windows
- Apple Support — back up iPhone: https://support.apple.com/en-in/HT203977

**Evidence note:** Do not claim survey results, audience impact, engagement rates, tool usage or experimental outcomes unless you actually collect and record them. Add screenshots and measured results only after performing the activities.
