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
        I am from Shaoguan, a city in southern China near Danxia Mountain, one of
        the classic landscapes associated with Danxia landforms. Growing up
        close to these rocks helped spark my curiosity about geology.

        I am now an early-career marine geologist interested in how Earth
        materials move through environments, resources, oceans, crust, and
        mantle. I use geochemistry, petrology, sedimentary records, and data
        synthesis to ask how natural systems work and how people relate to
        them.

        Outside research, I enjoy coffee, baking, LEGO, and staying active
        through hiking, swimming, and cycling.
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: About
        education: Education
        interests: Research Interests
    design:
      css_class: home-intro terrain-bg
      background:
        gradient_mesh:
          enable: false
      name:
        size: md
      avatar:
        size: large
        shape: rounded

  - block: markdown
    id: research
    content:
      title: Research
      subtitle: Earth material cycles across environments, oceans, and deep time
      text: |-
        I study how materials are produced, transported, transformed, and
        recycled across Earth's surface, oceans, crust, and mantle. My current
        work connects sedimentary basins, marine geology, ocean drilling, and
        isotope geochemistry to understand environmental change, resource
        formation, and deep Earth cycling.

        **Environmental and resource records.** Sedimentary basins preserve
        signals of paleogeography, organic matter enrichment, and environmental
        change. My earlier work in the South Poyang Basin used stratigraphic
        and geochemical records to reconstruct depositional environments and
        resource-related processes.

        **Carbon, water, and volatile cycling.** In the Makran system and
        related Pakistan magmatic belts, I examine how sediments, fluids, and
        melts transfer carbon, water, and trace elements from subducting plates
        into arc and collision-zone magmatism.

        **Ocean drilling and ocean-basin geochemistry.** I am developing new
        work on fresh South China Sea spreading-ridge basalt samples, combining
        radiogenic and stable isotope tracers to test how mantle sources,
        oceanic crust formation, and basin evolution shape material cycles in
        marginal seas.
    design:
      columns: '1'

  - block: collection
    id: publications
    content:
      title: Selected Publications
      text: Representative publications and manuscripts connected to the research themes above.
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2

  - block: collection
    id: projects
    content:
      title: Projects
      text: Case studies that connect environmental records, resource formation, ocean-basin evolution, and deep material recycling.
      filters:
        folders:
          - projects
    design:
      view: card
      columns: 3

  - block: markdown
    id: contact
    content:
      title: Contact & Collaboration
      subtitle: Ocean drilling, isotope geochemistry, and material cycling
      text: |-
        Email: [zengguangping22@mails.ucas.ac.cn](mailto:zengguangping22@mails.ucas.ac.cn)

        I am based in Guangzhou and currently affiliated with the South China
        Sea Institute of Oceanology, Chinese Academy of Sciences, and the Deep
        Sea Drilling Center, Guangzhou Marine Geological Survey.

        I welcome conversations about ocean drilling, marine geology, isotope
        geochemistry, carbon and volatile cycling, sedimentary records, and
        environmental or resource questions that connect field observations,
        laboratory data, and broader Earth-system problems.

        <iframe
          title="Guangzhou Marine Geological Survey location"
          src="https://www.google.com/maps?q=Guangzhou%20Marine%20Geological%20Survey&output=embed"
          width="100%"
          height="320"
          style="border:0; border-radius:12px; margin-top:1rem;"
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"
        ></iframe>
    design:
      columns: '1'
---
