---
Title: "Draconic Runecasting"
date: 2020-06-22T21:30:22-07:00
tags: ['homebrew', 'spell']

gallery:
    - title: Runes of Forming
      class: runes
      images:
        - source: /static/runes/form_of_protection.png
          caption: "Form of Protection: This form will concentrate arcane energy on the target to apply protective, bolstering and magnifying effects."
        - source: /static/runes/form_of_destruction.png
          caption: "Form of Destruction: This form will concentrate arcane energy on the target to apply destructive, enervating and reductive effects."
        - source: /static/runes/form_of_nullification.png
          caption: "Form of Nullification: Disrupt and repel arcane energy from the target."
    - title: Runes of Targeting
      class: runes
      images:
        - source: /static/runes/target_one.png
          caption: "Form of Target One: Apply arcane energy to a single target."
        - source: /static/runes/target_many.png
          caption: "Form of Target Many: Apply arcane energy to an area of effect."
    - title: Runes of Effect
      class: runes
      images:
        - source: /static/runes/effect_acid.png
          caption: "Form of Effect: Acid" 
        - source: /static/runes/effect_poison.png
          caption: "Form of Effect: Poison"
        - source: /static/runes/effect_necrotic.png
          caption: "Form of Effect: Necrotic" 
        - source: /static/runes/effect_psychic.png
          caption: "Form of Effect: Psychic" 
        - source: /static/runes/effect_binding.png
          caption: "Form of Effect: Binding" 
        - source: /static/runes/effect_levitate.png
          caption: "Form of Effect: Levitate" 
        - source: /static/runes/effect_bludgeoning.png
          caption: "Form of Effect: Bludgeoning" 
        - source: /static/runes/effect_piercing.png
          caption: "Form of Effect: Piercing" 
        - source: /static/runes/effect_slashing.png
          caption: "Form of Effect: Slashing" 
        - source: /static/runes/effect_force.png
          caption: "Form of Effect: Force" 
        - source: /static/runes/effect_cold.png
          caption: "Form of Effect: Cold" 
        - source: /static/runes/effect_fire.png
          caption: "Form of Effect: Fire" 
        - source: /static/runes/effect_lightning.png
          caption: "Form of Effect: Lightning" 
        - source: /static/runes/effect_thunder.png
          caption: "Form of Effect: Thunder" 
        - source: /static/runes/effect_haste.png
          caption: "Form of Effect: Haste" 
        - source: /static/runes/effect_invisible.png
          caption: "Form of Effect: Invisibility" 
        - source: /static/runes/effect_locate.png
          caption: "Form of Effect: Locate" 
        - source: /static/runes/effect_radiant.png
          caption: "Form of Effect: Radiant" 
        - source: /static/runes/effect_light.png
          caption: "Form of Effect: Light" 
        - source: /static/runes/effect_darkness.png
          caption: "Form of Effect: Darkness" 
        - source: /static/runes/effect_fear.png
          caption: "Form of Effect: Fear" 
        - source: /static/runes/effect_charm.png
          caption: "Form of Effect: Charm" 
        - source: /static/runes/effect_blind.png
          caption: "Form of Effect: Blind" 
        - source: /static/runes/effect_sleep.png
          caption: "Form of Effect: Sleep" 
        - source: /static/runes/effect_petrify.png
          caption: "Form of Effect: Petrify" 
        - source: /static/runes/effect_silence.png
          caption: "Form of Effect: Silence" 
        - source: /static/runes/effect_stun.png
          caption: "Form of Effect: Stun" 
        - source: /static/runes/effect_madness.png
          caption: "Form of Effect: Madness" 
        - source: /static/runes/effect_strength.png
          caption: "Form of Effect: Strength" 
        - source: /static/runes/effect_dexterity.png
          caption: "Form of Effect: Dexterity" 
        - source: /static/runes/effect_constitution.png
          caption: "Form of Effect: Constitution" 
        - source: /static/runes/effect_intelligence.png
          caption: "Form of Effect: Intelligence" 
        - source: /static/runes/effect_wisdom.png
          caption: "Form of Effect: Wisdom" 
        - source: /static/runes/effect_charisma.png
          caption: "Form of Effect: Charisma" 

      

statblock:
    category: spell
    name: Draconic Runecasting
    level: 1st
    school: Enchantment
    casting_time: 1 Action
    range: Touch, 5ft. sphere
    components: "V, S, M (Tools appropriate to surface as necessary: Woodworking tools, Smithing tools, etc)"
    duration: Until dispeled
    attack_or_save: "Attack (Melee)"
    effect: "Various (see description)"
    description: |
        When you cast this spell, you inscribe a glyph composed of Draconic Rune Forms that later unleashes a magical effect. You inscribe it either on a surface (such as a table or a section of floor or wall) or within an object that can be closed (such as a book, a scroll, or a treasure chest) to conceal the glyph. The glyph can cover an area no larger than 3 feet square.

        The glyph is nearly invisible and requires a successful Intelligence (Investigation) check against a DC of 17 to be found in full light, to a DC of 25 to be found in total darkness.

        On your turn you must draw the rune correctly without consulting the physical Book and show it to the DM, who will determine whether you have composed the rune correctly. Each rune must include a Form of Focus, a Form of Targeting and a Form of Effect as described in the physical Book. If your glyph includes the Form Of Target One, you must specify the target of the spell when you inscribe the glyph.

        **Failing to Compose The Rune Forms** If the DM determines that you have not correctly drawn the glyph, the glyph immediately erupts in an explosion of magical energy. All creatures in a sphere of 15ft radius must make a Dexterity saving throw. A creature takes 4d6 force damage and is pushed back 10 feet on a failed save, or half as much, and is not moved, on a successful one. The surface you were inscribing becomes permanently scorched and cannot be inscribed with another glyph.

        Any movement within 5 feet of the glyph will trigger the spell (if the movement is yours, you can choose to trigger the spell or not). This includes movement from visible creatures moving nearby as well as visible inanimate objects such as arrows, thrown items, moving the item on which the glyph is inscribed, and so on. Light level in the area has no impact on the trigger. When triggered, the glyph erupts with magical energy in a sphere centered on the glyph; the sphere has a radius of between and 5 and 15 feet, depending on the size of your glyph (glyph size in feet times five). The sphere spreads around corners.

        The effect of a triggered spell depends on the rune forms used:

        **Form of Destruction, Form of Target One** If your target is in range, they must make a Dexterity saving throw. A creature takes 3d8 damage on a failed saving throw or half as much damage on a successful one. For each additional level above 2nd, add an additional 1d8 damage (or half as much on saves).

        **Form of Destruction, Form of Target Many**  Each creature in the area must make a Dexterity saving throw. A creature takes 2d8 damage on a failed saving throw or half as much damage on a successful one. For each additional level above 1st, add an additional 1d8 damage (or half as much on saves).

        **Form of Protection, Form of Target One**  If your target creature is in range and willing, they gain the positive effect of the spell for one minute. There is no effect for additional spell levels.

        **Form of Protection, Form of Target Many**  Two willing creatures in the area gain the positive effect of the spell for one minute. For each additional spell level above 1st, two additional willing creatures in the area can be targeted. You choose the targets of the spell.

        **Form of Nullification, Form of Target One** If your target is in range, they must make a Dexterity saving throw. On a failed save, all magical effects on the target which match the rune's effect form are dispeled for 10 minutes. The nullification applies to all spell and potion effects on the target, as well as any enchanted items they have. Concentration spells affecting the target are immediately ended.

        **Form of Nullification, Form of Target Many**  The two creatures in the area closest to the glyph must make a Dexterity saving throw. On a failed save, all magical effects on the targets which match the rune's effect form are dispeled for 10 minutes. The nullification applies to all spell and potion effects on the targets, as well as any enchanted items they have. Concentration spells affecting the targets are immediately ended. For each spell level above 1st, two additional creatures in the area are targeted.

        **Charging Glyphs** Glyphs successfully inscribed are charged at 1st level. You can increase the spell level by spending 2 sorcery points to increase the level by 1, to a maximum of your current spellcasting level. Once a glyph's spell is triggered, the magical effect is expended and the glyph becomes inert. Inert glyphs can be recharged as a bonus action, using 2 sorcery points per spell level.

        **Destroying Glyphs** Once inscribed, a glyph remains intact until its form is disturbed (shattering the wood it's etched into, covering a painted glyph with new paint, stepping on a rune drawn in dirt, etc). You (and only you) can choose to destroy a charged glyph without triggering the spell effect in this way.

        ## The Book of Runes

        Below is a record of the Draconic Rune Forms known to modern Telisaran scholars. It is not known if this represents a complete Book of Runes; some scholars point to missing forms that might be made by mirroring or rotating existing forms as evidence that this is an incomplete record, but little research into the Book of Runes has survived into the Modern Era.

        **Subtle Storytelling** Advanced spellcasters can move beyond the gross effects to the subtle, by weaving glyphs together with will and intent. In the Dragonborn tradition this is often done with storytelling, where the caster speaks aloud a story as the glyph is formed. In this manner, rune forms for necromancy may be turned not just to necrotic energy, but to summoning or turning the undead also, while the rune forms for fire and cold may be tempered to provide a high degree of control over ambient temperature, warming a home as a hearth or cooling a food store. Casters may attempt to employ this mechanic at the discretion of the DM, who may call for Arcana checks in addition to ajudicating the glyph.

        **Studying the Book** At the DM's discretion, players granted a Book of Runes may study the Runes of Effect using Arcana checks and so on, or by combining runes into charged glyphs and witnessing the effects. 

---
The Dragonborn of Telisar had a highly advanced magical tradition millenia before others. Runecasting consists of the arrangement of individual runes into complex forms that focus and channel raw magical energies into coherent spells. The complete system is referred to as the Book of Runes, and is a closely guarded secret amongst the First People. However, should a sorcerer of draconic descent gain access to the Book, either by careful study or reckless experimentation the wisdom of this tradition might be harnessed.

Dragonborn children are often gifted the Book of Runes, a complete set of illustrated runes, each one etched and painted onto a 3x3" glass tile, and given instruction in their use by combining and stacking the tiles to study completed glyphs of power safely. The Book is also used in a variety of leisure games, much as the younger races use cards, though little of the particulars are known outside the First People.
