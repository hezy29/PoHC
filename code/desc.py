mod1 = """
# measurement 
informed =~ motiv + priv + big_data + pcp
trust =~ govern_trust_pub + govern_trust_hc + doubt_hc
policy_effect =~ smart_hc + benef_hc + effec_hc + matur_hc
privacy_concern =~ govern_viola_priv + unnece + sec_hand_used + viola_priv
emo =~ satis_used + satis_grade + diss_manda_hc + dislike_hc
behaviour =~ used_now + used_after

# regressions
trust ~ informed
privacy_concern ~ trust
emo ~ policy_effect + privacy_concern
behaviour ~ informed + trust + policy_effect + privacy_concern + emo

# residual correlations

"""
