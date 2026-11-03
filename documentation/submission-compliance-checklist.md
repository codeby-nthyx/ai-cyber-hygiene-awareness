# Submission Compliance Checklist

**Project:** AI Cyber Hygiene Awareness Campaign for Students  
**Audience:** Students aged 15–24, especially non-technical learners  
**Audit date:** 2026-11-03  
**Submission format:** GitHub repository

This checklist maps the project brief to the current repository and separates completed deliverables from evidence that still needs to be captured. A file existing in the repository is not proof that a tool was used or an activity was performed.

## Requirement-by-requirement audit

| Requirement | Evidence / location | Status |
|---|---|---|
| Select cyber-hygiene topics relevant to students | Five topics are defined in the research report and repeated across campaign assets. | Complete |
| Research using at least two AI tools | NotebookLM and Perplexity are recorded as used in `ai-tools-and-skills-register.md`; preserve screenshots/notes showing actual use. | Content recorded; usage evidence to retain |
| Verify research against official/reputable sources | Research report, article references and claim-level verification register. | Complete in project documentation; keep source-access evidence if required |
| Research summary/report | `research/research-report.md` (approximately 1,068 words). | Complete |
| Article of at least 1,000 words | `content/awareness-article.md` (approximately 1,417 words including headings/references). | Complete |
| Six social-media posts | `content/social-media-posts.md` contains six posts. | Complete |
| Poster/infographic | Editable Canva infographic linked in the root README. | Complete |
| 5–7-slide presentation | Editable Canva presentation; Canva metadata confirms 7 pages. | Complete |
| 30–60-second awareness video script or short clip | `content/video-script-storyboard.md` contains timed scenes, visuals, on-screen text and full voice-over; target runtime is 53 seconds. The brief permits a script, so a rendered MP4 is not required. | Complete via script option |
| Ten-question quiz with answer key | `content/quiz.md` contains 10 MCQs, answers, explanations and a scoring guide. | Complete |
| Automate one project step | `automation/generate_tip_drafts.py` converts the CSV to Markdown; generated output is committed in `automation/generated_posts.md`. | Complete |
| Test/document inaccurate or misleading AI advice | `documentation/verification-and-error-analysis.md` records claim checks and common error patterns with corrections. | Complete as documented review |
| Prompt engineering / prompt library | `documentation/prompt-library.md` contains eight reusable prompts. | Complete |
| At least six AI skills | `documentation/ai-tools-and-skills-register.md` records nine skills. | Complete |
| At least four AI tools | The register records ChatGPT, Canva, NotebookLM and Perplexity as AI tools used. Python 3 is the automation runtime, not counted as an AI tool. | Complete in register; preserve usage evidence |
| Before/after comparison | `documentation/before-after-analysis.md` compares five initial and revised claims and states that the comparison is qualitative, not a measured experiment. | Complete |
| Responsible AI, privacy and limitations | `documentation/responsible-ai-and-limitations.md`. | Complete |
| Live demonstration | Not included in the final repository deliverables under the user's later-confirmed repo-only submission scope. | Not applicable to this submission |

## Evidence still to preserve outside the written deliverables

- Screenshots or exports showing the actual NotebookLM and Perplexity research sessions/source notebooks.
- Representative ChatGPT prompt/output evidence, with private data excluded.
- A terminal screenshot showing the Python automation command and successful output, if the evaluator asks for execution proof.
- Final exported copies or accessible view links for the Canva presentation and infographic.

Do not fabricate or backdate evidence. The project files document the workflow, but screenshots/exports should only be added after the corresponding activity has actually been performed and captured.

## Final consistency checks

- Keep the video deliverable described as a **script/storyboard**, not a completed video.
- The presentation, infographic and repository should use the same five habits and avoid stronger claims than the verified source wording.
- Do not claim survey results, audience impact, engagement metrics or learning gains; no such study is recorded.
- Recheck source pages and platform-specific settings before reuse because guidance and interfaces can change.

## Overall result

The repository contains the required written, visual, presentation, quiz, automation and documentation deliverables. The video requirement is satisfied through the expressly permitted script option. The remaining submission task is to preserve genuine evidence of AI-tool use and automation execution if the evaluator requires screenshots or logs; these cannot be generated retrospectively from the repository contents alone.
