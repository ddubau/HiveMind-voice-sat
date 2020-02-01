from voice_satellite.configuration import CONFIGURATION
from voice_satellite import JarbasVoiceTerminal, platform
from jarbas_hive_mind import HiveMindConnection


def connect_to_hivemind(config=CONFIGURATION, host="127.0.0.1",
                        port=5678, name="JarbasVoiceTerminal",
                        key="voice_key", useragent=platform):
    con = HiveMindConnection(host, port)

    terminal = JarbasVoiceTerminal(config=config, headers=con.get_headers(name, key),
                                   useragent=useragent)

    con.secure_connect(terminal)


if __name__ == '__main__':
    # TODO argparse
    connect_to_hivemind()
