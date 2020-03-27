import subprocess
import optparse


def change_mac(interface, new_mac):
    print("$ Changing mac address " + interface + " to " + new_mac)
    subprocess.call(['ipconfig', interface, 'down'])
    subprocess.call(['ipconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ipconfig', interface, 'up'])


def get_argument():
    parser = optparse.OptionParser()

    parser.add_option('-i', '--interface', dest='interface',
                      help="it will change interface wlan0")

    parser.add_option('-m', '--mac', dest='new_mac',
                      help="it will change Mac Address")
    return parser.parse_args()


(options, arguments) = get_argument()
change_mac(options.interface, options.interface)
