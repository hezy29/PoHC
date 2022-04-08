mod_basic = """
# measurement 
informed =~ motiv + priv + big_data + pcp
DEFINE(ordinal) motiv priv big_data pcp 

trust =~ govern_trust_pub + govern_trust_hc + doubt_hc
DEFINE(ordinal) govern_trust_pub govern_trust_hc doubt_hc

policy_effect =~ smart_hc + benef_hc + effec_hc + matur_hc
DEFINE(ordinal)  smart_hc benef_hc effec_hc matur_hc

privacy_concern =~ govern_viola_priv + unnece + sec_hand_used + viola_priv
DEFINE(ordinal) govern_viola_priv unnece sec_hand_used viola_priv 

emo =~ satis_used + satis_grade + diss_manda_hc + dislike_hc
DEFINE(ordinal) satis_used satis_grade diss_manda_hc dislike_hc

behaviour =~ used_now + used_after
DEFINE(ordinal) used_now used_after


# regressions
trust ~ informed
privacy_concern ~ trust
emo ~ policy_effect + privacy_concern
behaviour ~ informed + trust + policy_effect + privacy_concern + emo


# residual correlations
# motiv, priv, big_data, pcp ~~ motiv + priv + big_data + pcp
# govern_trust_pub, govern_trust_hc, doubt_hc ~~ govern_trust_pub + govern_trust_hc + doubt_hc
# smart_hc, benef_hc, effec_hc, matur_hc ~~ smart_hc + benef_hc + effec_hc + matur_hc
# govern_viola_priv, unnece, sec_hand_used, viola_priv ~~ govern_viola_priv + unnece + sec_hand_used + viola_priv 
# satis_used, satis_grade, diss_manda_hc, dislike_hc ~~ satis_used + satis_grade + diss_manda_hc + dislike_hc
# used_now, used_after ~~ used_now + used_after
# behaviour, informed, trust, policy_effect, privacy_concern, emo ~~ behaviour + informed + trust + policy_effect + privacy_concern + emo
"""

mod_fixed = """
# measurement 
informed =~ motiv + priv + big_data + pcp
DEFINE(ordinal) motiv priv big_data pcp 

trust =~ govern_trust_pub + govern_trust_hc 
DEFINE(ordinal) govern_trust_pub govern_trust_hc 

policy_effect =~ smart_hc + benef_hc + effec_hc + matur_hc
DEFINE(ordinal)  smart_hc benef_hc effec_hc matur_hc

privacy_concern =~ govern_viola_priv + unnece + sec_hand_used + viola_priv
DEFINE(ordinal) govern_viola_priv unnece sec_hand_used viola_priv 

emo =~ satis_used + satis_grade + diss_manda_hc + dislike_hc
DEFINE(ordinal) satis_used satis_grade diss_manda_hc dislike_hc

behaviour =~ used_now + used_after
DEFINE(ordinal) used_now used_after


# regressions
trust ~ informed
privacy_concern ~ trust
emo ~ policy_effect + privacy_concern
behaviour ~ informed + trust + policy_effect + privacy_concern + emo


# residual correlations
# motiv, priv, big_data, pcp ~~ motiv + priv + big_data + pcp
# govern_trust_pub, govern_trust_hc, doubt_hc ~~ govern_trust_pub + govern_trust_hc + doubt_hc
# smart_hc, benef_hc, effec_hc, matur_hc ~~ smart_hc + benef_hc + effec_hc + matur_hc
# govern_viola_priv, unnece, sec_hand_used, viola_priv ~~ govern_viola_priv + unnece + sec_hand_used + viola_priv 
# satis_used, satis_grade, diss_manda_hc, dislike_hc ~~ satis_used + satis_grade + diss_manda_hc + dislike_hc
# used_now, used_after ~~ used_now + used_after
# behaviour, informed, trust, policy_effect, privacy_concern, emo ~~ behaviour + informed + trust + policy_effect + privacy_concern + emo
"""
