---
Title: "{{ humanize .Name | title }}"
date: {{ .Date }}
tags: ['homebrew', 'spell']
markup: md

statblock:
    name: "{{ humanize .Name | title }}"
    school:

---

{{< item >}}

**Level** 1st

**Casting Time** 1 Action

**Range/Area** Touch, 5ft

**Components** V, S, M

**Duration** 1 minute

**School** Enchantment

**Attack/Save** Attack (Melee)

**Damage/Effect** Fire damage

{{< /item >}}
