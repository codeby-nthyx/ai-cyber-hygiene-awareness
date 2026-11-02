# Local content automation

## Purpose
The Python script converts structured, human-reviewed campaign tips in `tips.csv` into Markdown draft posts. This demonstrates a repeatable automation step without automatically publishing content.

## Requirements
- Python 3.10 or later
- Python standard library only

## Run
From the repository root:

```bash
python automation/generate_tip_drafts.py
```

Expected output: `automation/generated_posts.md`.

## Workflow
1. Review the claims and caveats in `tips.csv` against the campaign's source list.
2. Run the script.
3. Inspect the generated Markdown.
4. Edit for the intended platform and audience.
5. Obtain human approval before publication.

The script does not browse, verify sources, post to social media or measure engagement. A successful run is not evidence that the underlying claims are true.
