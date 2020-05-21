---
Title: "{{ humanize .Name | title }}"
date: {{ .Date }}
tags: ['homebrew', 'monster']
markup: md

statblock:
    name: "{{ humanize .Name | title }}"
    size: medium
    type: beast
    alignment: unaligned
    AC: 10
    HP: 100 (10d10 + 50)
    speed: 30ft
    STR: 10,0
    DEX: 10,0
    CON: 10,0
    INT: 10,0
    WIS: 10,0
    CHA: 10,0
    skills:
    saving_throws:
    resistances:
    damage_immunities:
    condition_immunities: 
    senses: Passive Perception 10
    languages: Common
    cr:
---

Flavour text goes here

{{< monster >}}

**Attribute** Description

## Actions

**Action** *ActionType* +1 to hit, reach 5 ft., one target. Hit: 5 (2d4) DamageType damage.

## Legendary Actions

**Attribute** Description

## Reactions

**Attribute** Description

## Legendary Reactions

**Attribute** Description

## Lair and Lair Actions

**Attribute** Description

{{< /monster >}}
