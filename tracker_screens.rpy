screen tracker_home():
    tag phone_tag
    modal True

    python:
        TrackerData.data = []

        TrackerData(amber, v1_amber_clean, _("• I helped Amber get off drugs."))
        TrackerData(amber, "v1_amber" in viewed_scenes, _("• I let Amber do drugs and had sex."))
        TrackerData(amber, "v2_amber" in viewed_scenes, _("• Amber gave me a blowjob at Lauren's party."))
        TrackerData(amber, v2s42_flirt, _("• I flirted with Amber during our investigation."))
        TrackerData(amber, v3s20_take_twazzlers, _("• I brought Amber her favorite snack - Twazzlers!"))
        TrackerData(amber, v3s23_support_amber, _("• I supported Amber's decision to become a stripper."))

        TrackerData(aubrey, "v11_aubrey" in viewed_scenes, _("• Aubrey and I became FWB."))
        TrackerData(aubrey, v0s13_rejected_aubrey, _("• I turned down Aubrey for the \"Mile High club\"."))
        TrackerData(aubrey, v0s48_canoeing_as_date, _("• Aubrey and I went canoeing."))
        TrackerData(aubrey, v0_aubrey_concert, _("• We went to Polly's concert together."))
        TrackerData(aubrey, "v14_threesome" in viewed_scenes, _("• I had a threesome with Riley and Aubrey."))
        TrackerData(aubrey, v1s31b_smoke_weed_with_aubrey, _("• I smoked weed with Aubrey."))
        TrackerData(aubrey, v2_RileyUpset, _("• I agreed with Aubrey - Monogamy is the way."))
        TrackerData(aubrey, v2s9_wedding_date, _("• Aubrey agreed to a wedding date."))
        TrackerData(aubrey, v2s18_mention_list_aubrey, _("• I mentioned Imre's party checklist to Aubrey."))
        TrackerData(aubrey, "v2_aubrey" in viewed_scenes, _("• I fingered Aubrey at Lauren's party."))
        TrackerData(aubrey, v2s33_take_photo, _("• I took the photo of Aubrey with her family."))
        TrackerData(aubrey, v3_aubrey_date, _("• Aubrey suggested we go on a real date."))

        TrackerData(autumn, v0_visited_shelter, _("• I visited Autumn at the dog shelter."))
        TrackerData(autumn, v0_signs, _("• I helped Autumn create signs for the protest."))
        TrackerData(autumn, v0_protest, _("• I joined Autumn for the protest."))
        TrackerData(autumn, v2_autumn_lunchbreak, _("• I helped Autumn for the dog shelter's grand reopening."))
        TrackerData(autumn, v2_autumn_freemug, _("• I asked Autumn for a free mug."))
        TrackerData(autumn, v2_autumn_smoke, _("• I smoked weed with Autumn."))
        TrackerData(autumn, v2s18a_showlist_penelope_autumn, _("• I showed Autumn Imre's party checklist."))
        TrackerData(autumn, "v2_autumn" in viewed_scenes, _("• Autumn and I kissed at Lauren's party."))
        TrackerData(autumn, (not CharacterService.is_mad(autumn)), _("• Autumn trusts me."))
        TrackerData(autumn, v2s36_not_good_idea, _("• I didn't take up Autumn on having sex."))
        TrackerData(autumn, v2s36_autumn_kiss, _("• I kissed Autumn."))

        TrackerData(chloe, "v1_chloe" in viewed_scenes, _("• I had sex with Chloe in the school parking lot."))
        TrackerData(chloe, v1_help_chloe, _("• I told Chloe I would help with her campaign."))
        TrackerData(chloe, v1s23_agree, _("• I agreed to help Chloe with campaign photos."))
        TrackerData(chloe, v1s31bTrustChloe, _("• I trusted Chloe to meet with Grayson."))
        TrackerData(chloe, v1s41a_standup, _("• I stood up against the Apes posting Chloe's lewds on Kiwii."))
        TrackerData(chloe, v1_ApesPostChloePics, _("• The Apes posted Chloe's lewds on Kiwii."))
        TrackerData(chloe, v2s7_chloe_empathize, _("• I was empathetic with Chloe about her campaign crisis"))
        TrackerData(chloe, v3_parent_chloe, _("• I partnered with Chloe for our parenting assignment."))
        TrackerData(chloe, "v3_chloe" in viewed_scenes, _("• Chloe and I were bad parents and had sex."))
        TrackerData(chloe, v3_chloe_mc_masseuse, _("• I agreed to be the masseuse for Chloe's spa night."))
        TrackerData(chloe, v3s64_confessed_insult, _("• I confessed to writing the suggestion card."))

        TrackerData(emily, "v13_emily" in viewed_scenes, _("• I had angry sex with Emily in Europe."))
        TrackerData(emily, v1_emily_ily, _("• I told Emily that I love her."))
        TrackerData(emily, "v2_emily" in viewed_scenes, _("• I sexted with Emily."))
        TrackerData(emily, "v3_emily" in viewed_scenes, _("• Emily showed off her new lingerie on webcam."))

        TrackerData(jenny, "v1_jenny" in viewed_scenes, _("• I had sex with Jenny at the lagoon."))

        TrackerData(lauren, v0_lauren_too_far, _("• I went too far with Lauren at the movies."))
        TrackerData(lauren, v0_lauren_caught_aubrey, _("• Lauren caught me and Aubrey having sex on the plane."))
        TrackerData(lauren, v0_told_lauren, _("• I told Lauren about me and Aubrey."))
        TrackerData(lauren, "v12_lauren" in viewed_scenes, _("• I slept with Lauren for the first time in Europe."))
        TrackerData(lauren, v1_lauren_helps_lindsey, _("• I convinced Lauren to help Lindsey's campaign."))
        TrackerData(lauren, v1_lauren_sabotage, _("• I convinced Lauren to sabatoge Lindsey's campaign."))
        TrackerData(lauren, v1s46a_love_lauren_more, _("• I told Lauren you love her \"even more than before\" she started to become more sexual."))
        TrackerData(lauren, "v2_lauren" in viewed_scenes and not v2s18e_cum_in_lauren, _("• I had sex with Lauren at her party."))
        TrackerData(lauren, "v2_lauren" in viewed_scenes and v2s18e_cum_in_lauren, _("• I had sex with Lauren at her party and came inside her."))
        TrackerData(lauren, "v3_lauren" in viewed_scenes, _("• Lauren gave me a handjob during Ms. Rose's class."))

        TrackerData(lindsey, v1_help_lindsey, _("• I told Lindsey I would help with her campaign."))
        TrackerData(lindsey, v2_lindsey_alcohol, _("• I got alcohol for Lindsey's party."))
        TrackerData(lindsey, v3_polly_endorsement, _("• We got Polly to endorse Lindsey's campaign."))
        TrackerData(lindsey, "v3_lindsey" in viewed_scenes, _("• I has sex with Lindsey during her massage."))

        TrackerData(ms_rose, "v12_rose" in viewed_scenes, _("• I has sex with Ms. Rose in Europe."))
        TrackerData(ms_rose, v2_mad_at_ms_rose, _("• I'm angry at Ms. Rose."))
        TrackerData(ms_rose, v2_seduce_ms_rose, _("• I seduced Ms. Rose during Chloe's campaign meeting."))
        TrackerData(ms_rose, v2_threaten_ms_rose, _("• I threatened Ms. Rose during Chloe's campaign meeting."))
        TrackerData(ms_rose, "v2_rose" in viewed_scenes, _("• I had sex again with Ms. Rose."))
        TrackerData(ms_rose, v3_opera_invite, _("• I forgave Ms. Rose."))
        TrackerData(ms_rose, v3_ms_rose_breakup, _("• I ended things with Ms. Rose."))

        TrackerData(naomi, v2s33_flirt, _("• I flirted with Naomi at Aubrey's parent's wedding."))
        TrackerData(naomi, "v2_naomi" in viewed_scenes, _("• Naomi gave me a blowjob at her parents' wedding."))

        TrackerData(nora, v2_NoraFriendzone, _("• Nora is in the friendzone."))
        TrackerData(nora, v0_help_nora_freeroam, _("• I helped Nora hand out fliers."))
        TrackerData(nora, v0_chase_robber and not v0_fight_win, _("• I chased the robber."))
        TrackerData(nora, v0_chase_robber and v0_fight_win, _("• I chased the robber and beat him."))
        TrackerData(nora, "v12_nora" in viewed_scenes, _("• I slept with Nora in Europe."))
        TrackerData(nora, v2_blame_nora, _("• I blame Nora for the brakeup with Chris."))
        TrackerData(nora, v2s48_follow_your_heart, _("• I told Nora to follow her heart."))
        TrackerData(nora, "v2_nora" in viewed_scenes, _("• I slept with Nora at her dad's cabin."))
        TrackerData(nora, v2_nora_cum, _("• I came inside Nora."))
        TrackerData(nora, "v3_nora" in viewed_scenes, _("• I fingered Nora during her massage."))

        TrackerData(riley, "v14_threesome" in viewed_scenes, _("• I had a threesome with Riley and Aubrey."))
        TrackerData(riley, "v2_riley" in viewed_scenes, _("• Riley gave me a handjob at Lauren's party."))
        TrackerData(riley, (CharacterService.is_fwb(riley)), _("• I agreed with Riley - Polygamy is the way."))
        TrackerData(riley, "v3_riley" in viewed_scenes, _("• Riley gave me a blowjob after my fight with Tom."))
        TrackerData(riley, v3s11_sign_up, _("• I signed up for the Newspaper sqaud with Riley."))

        TrackerData(penelope, v0_bowling, _("• I went bowling with Penelope."))
        TrackerData(penelope, v0_pen_goes_europe, _("• I was able to get Penelope to go to Europe."))
        TrackerData(penelope, v0_penelope_concert, _("• Penelope and I went to Polly's concert together."))
        TrackerData(penelope, v1s37_focus_on_us, _("• I helped Penelope stay focused during your date."))
        TrackerData(penelope, v1s39_id_wait, _("• I told Penelope that you'd wait to say something in private."))
        TrackerData(penelope, v1_PenRomScene, _("• I acted out a romantic scene with Penelope."))
        TrackerData(penelope, v1_pen_argument_scene, _("• I acted out an argument scene with Penelope."))
        TrackerData(penelope, v2s18a_showlist_penelope_autumn, _("• I showed Penelope Imre's party checklist."))
        TrackerData(penelope, "v2_penelope" in viewed_scenes, _("• I went down on Penelope at Lauren's party."))
        TrackerData(penelope, v1_penelope_date, _("• Penelope and I went on a dinner date."))
        TrackerData(penelope, "v3_penelope" in viewed_scenes, _("• Penelop and I had sex while dog sitting."))

        TrackerData(samantha, v0_invite_sam_europe, _("• I invited Sam to Europe."))
        TrackerData(samantha, v0_invite_samantha, _("• I invited Sam on the weed bus tour."))
        TrackerData(samantha, v1_badsinging_Sam, _("• I joked about Samantha's singing."))
        TrackerData(samantha, v1_SamanthaDrugs, _("• I let Samantha use drugs."))
        TrackerData(samantha, "v1_samantha" in viewed_scenes, _("• I slept with Samantha."))
        TrackerData(samantha, v1_samantha_cum, _("• I came inside Samantha."))

    use base_phone("tracker_background"):
        fixed:
            pos (12, 6)
            ysize 128

            imagebutton:
                idle "phone_back_button"
                action Show("phone")
                xpos 20
                yalign 0.75

        vpgrid:
            cols 3
            spacing 18
            xalign 0.5
            ypos 170
            allow_underfull True

            for npc in sorted(set(data.character for data in TrackerData.data), key=lambda npc: npc.name):
                imagebutton:
                    idle Transform(npc.profile_picture, size=(117, 117), matrixcolor=BrightnessMatrix(0))
                    hover Transform(npc.profile_picture, size=(117, 117), matrixcolor=BrightnessMatrix(0.2))
                    action Show("tracker_choices", character=npc)


screen tracker_choices(character):
    tag phone_tag
    modal True

    use base_phone("tracker_info_background"):
        frame:
            ysize 95
            ypos 63

            imagebutton:
                idle "phone_back_button"
                action Show("tracker_home")
                xpos 25
                yalign 0.5

            text character.name:
                style "message_text"
                size 42
                align (0.5, 0.5) 

        viewport:
            yadjustment inf_adj
            mousewheel True
            ysize 685
            ypos 158

            vbox:
                xalign 0.5

                for data in TrackerData.data:
                    if data.character == character and data.condition:
                        frame:
                            padding (40, 30)
                            background "phone_message_background"

                            text data.true_text style "message_text"


style tracker_name is text:
    color "#fff"
    font "fonts/Montserrat-ExtraBold.ttf"
    size 18

style tracker_text is text:
    color "#fff"
    font "fonts/Montserrat-SemiBold.ttf"
    size 15

style tracker_locked_name is text:
    color "#777"
    font "fonts/Montserrat-ExtraBold.ttf"
    size 18
