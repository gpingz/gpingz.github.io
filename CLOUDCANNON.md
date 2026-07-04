# CloudCannon Editing Guide

This site is prepared for CloudCannon editing. CloudCannon should connect to the
GitHub repository:

`gpingz/gpingz.github.io`

Public site:

`https://gpingz.github.io/`

## Connect The Repository

1. Sign in to CloudCannon.
2. Create a new site.
3. Choose GitHub as the source.
4. Select `gpingz/gpingz.github.io`.
5. Use the root of the repository as the site source.
6. Keep the build output folder as `public`.

The repository already contains `cloudcannon.config.yml`, so CloudCannon should
show editable sections for profile data, the homepage, projects, publications,
and uploads.

## Build Settings

Use these settings if CloudCannon asks for them:

- Static site generator: Hugo
- Install command: `pnpm install --no-frozen-lockfile`
- Build command: `hugo --gc --minify && pnpm run pagefind`
- Output folder: `public`
- Hugo version: `0.163.3`
- Node version: `22`

GitHub Pages is still the public host. After CloudCannon saves changes to
GitHub, GitHub Actions will rebuild and publish the site automatically.

## Replace The Profile Photo

Replace this file:

`assets/media/authors/me.png`

Use a square image when possible. A 1024 x 1024 PNG or JPG works well.

## Replace Project Field Photos

Each project uses a `featured.jpg` file in its own folder:

- `content/projects/makran-carbon-cycling/featured.jpg`
- `content/projects/pakistan-cenozoic-volcanism/featured.jpg`
- `content/projects/south-poyang-basin/featured.jpg`

Recommended image shape: landscape, around 1400 x 1050 px or larger.

## Edit Profile Text

Open the Profile data section and edit:

`data/authors/me.yaml`

Common fields:

- `role`
- `bio`
- `affiliations`
- `interests`
- `education`
- `experience`
- `skills`
- `awards`

## Edit Homepage Text

Open the Homepage collection and edit:

`content/_index.md`

Common sections:

- About text in the first `resume-biography-3` block
- Research section text
- Contact section text

## Edit Project Descriptions

Open the Projects collection. Each project has:

- `title`
- `summary`
- `tags`
- main Markdown body below the front matter

CloudCannon saves changes back to GitHub as commits. Wait for the GitHub Pages
workflow to finish before checking the public website.
