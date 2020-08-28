---
Title: "{{ humanize .Name | title }}"
date: {{ .Date }}
tags: ['homebrew', 'spell']
markup: md

statblock:
    category: spell
    name: "{{ humanize .Name | title }}"
    level: 1st
    school:
    casting_time: 1 Action
    range: Touch
    components: "V, S, M (a lock of hair)"
    duration: instant
    attack_or_save: "Attack (Melee)"
    effect: "Fire Damage"
    description:
---


