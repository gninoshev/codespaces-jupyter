ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

ospf_data = ospf_route.split()

ospf_data[1] = ospf_data[1].strip("[ ]")
ospf_data[3] = ospf_data[3].strip(",")
ospf_data[4] = ospf_data[4].strip(",")


result = f"{'Prefix':<20} {ospf_data[0]:<20}\n" \
            f"{'AD/Metric':<20} {ospf_data[1]:<20}\n" \
            f"{'Next-Hop':<20} {ospf_data[3]:<20}\n" \
            f"{'Last update':<20} {ospf_data[4]:<20}\n" \
            f"{'Outbond interface':<20} {ospf_data[5]:<20}"

print(result)
