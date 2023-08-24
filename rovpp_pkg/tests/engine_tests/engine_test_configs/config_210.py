from frozendict import frozendict

from bgpy.tests.engine_tests.graphs import graph_030
from bgpy.tests.engine_tests.utils import EngineTestConfig

from bgpy.simulation_engine import BGPSimpleAS
from bgpy.enums import ASNs
from bgpy.simulation_framework import ScenarioConfig, SubprefixHijack

from rovpp_pkg import ROVPPAnn, ROVPPV2aSimpleAS

config_210 = EngineTestConfig(
    name="210",
    desc="",
    scenario_config=ScenarioConfig(
        ScenarioCls=SubprefixHijack,
        BaseASCls=BGPSimpleAS,
        AdoptASCls=ROVPPV2aSimpleAS,
        AnnCls=ROVPPAnn,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict({
            4: ROVPPV2aSimpleAS,
            10: ROVPPV2aSimpleAS,
            ASNs.VICTIM.value: ROVPPV2aSimpleAS,
        })
    ),
    graph=graph_030,
    propagation_rounds=1,
)
