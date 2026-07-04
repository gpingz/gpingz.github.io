---
title: ''
summary: 'Academic homepage of Dr. Guangping Zeng'
date: 2026-07-04
type: landing

sections:
  - block: resume-biography-3
    content:
      username: me
      text: |
        Marine geologist studying volatile cycling in subduction zones, isotope
        geochemistry, thermodynamic modeling, and subduction-to-collision
        magmatism.
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: About
        education: Education
        interests: Research Interests
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: large
        shape: circle

  - block: markdown
    id: research
    content:
      title: Research
      subtitle: Volatile cycling in subduction zones
      text: |-
        My research focuses on volatile (CO<sub>2</sub> and H<sub>2</sub>O)
        cycling in subduction zones and its role in magma generation and
        metallogenesis. I use isotope geochemistry and thermodynamic modeling
        to constrain volatile cycling processes in the Makran system, an
        atypical low-angle subduction zone in the northern Arabian Sea with
        exceptionally thick sediment inputs.

        I am extending this work with big-data and machine-learning approaches
        to compare subduction systems globally and test how sediment inputs,
        fluids, and melts shape arc geochemistry.
    design:
      columns: '1'

  - block: collection
    id: publications
    content:
      title: Featured Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2

  - block: collection
    content:
      title: Recent Publications
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation

  - block: collection
    id: projects
    content:
      title: Projects
      text: Selected research directions from subduction-zone carbon cycling to basin paleogeography.
      filters:
        folders:
          - projects
    design:
      view: card
      columns: 3

  - block: markdown
    id: contact
    content:
      title: Contact
      subtitle: Collaboration and research inquiries
      text: |-
        Email: [zengguangping22@mails.ucas.ac.cn](mailto:zengguangping22@mails.ucas.ac.cn)

        South China Sea Institute of Oceanology, Chinese Academy of Sciences

        Deep Sea Drilling Center, Guangzhou Marine Geological Survey
    design:
      columns: '1'
---
