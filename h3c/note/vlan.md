#  keyword

h3c vlan

h3c 6850 vlan

# references

https://www.h3c.com/en/Support/Resource_Center/HK/Home/WLAN/00-Public/Configure___Deploy/Configuration_Guides/H3C_AC_CG(E3703P61_R3509P61)-6W102/03/201905/1178303_294551_0.htm

https://www.h3c.com/en/Support/Resource_Center/EN/Home/Switches/00-Public/Configure___Deploy/Configuration_Examples/H3C_S6850_S9850_S9820-64H_CE-6W100/202002/1273932_294551_0.htm

# vlan

	**vlan** { *vlan-id1* [ **to** *vlan-id2* ] | **all** }
	
[S1]vlan 10
[S1]vlan 20 to 30
[S1]vlan all
[S1]undo vlan 2 to 4094


[S1-vlan10]name manager
[S1-vlan10]description "This vlan is a manage vlan"

[S1]display vlan brief
[S1]display vlan 10
[S1]display vlan

## access


