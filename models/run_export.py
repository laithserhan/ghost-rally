import os
from subprocess import Popen, PIPE
import re
import tempfile

local_dir = os.path.dirname(os.path.realpath(__file__))
blender_dir = os.path.expandvars("%programfiles%/Blender Foundation/Blender")

def call(args):
    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    exitcode = proc.returncode
    #
    return exitcode, out, err

# file_list = ['deathstar','junk2','tie','xwing','ywing','title','turret','trench1','vent','mfalcon','generator','tiex1']
# file_list = ['audi','audi_bbox','vtree']
file_list = ['205gti','205gti_bbox']
s = "{:02x}".format(len(file_list))
for blend_file in file_list:
    print("Exporting: {}.blend".format(blend_file))
    fd, path = tempfile.mkstemp()
    try:
        os.close(fd)
        exitcode, out, err = call([os.path.join(blender_dir,"blender.exe"),os.path.join(local_dir,blend_file + ".blend"),"--background","--python",os.path.join(local_dir,"blender_export_uv.py"),"--","--out",path])
        if err:
            raise Exception('Unable to loadt: {}. Exception: {}'.format(blend_file,err))
        print("exit: {} \n out:{}\n err: {}\n".format(exitcode,out,err))
        with open(path, 'r') as outfile:
            s = s + outfile.read()
    finally:
        os.remove(path)

# extra data
s = s + "ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ce0008860948f70008880948c900088809489c00088709118612510948c700088a09489a00088709118812820948c5000809118812518b09488800088709118f12830948c40082098a12518b09488600088709119012518309c40082099512518809119812518209c40082099612518609119a12510948c3008209b0120a4a8712510948c100080911af120a82094a8712820948bf0008091187120a4aa0120a8a094a8612830948be00820987120a82094a9e120a8c098612518309be00820986120a0901418b094a8c120a87090188004182098712518209be008209861282098200418b094a8a120a8709018a0041094a8712510948bd008209861282098d00418c0901920041094a8712510948bc008209861282098e00418a0901940082094a8712820948bb00820986128209ae0083094a8612830948ba00820986128209ae004183098612518309ba00820986128209af004182098712518209b90008091185120a0901b00041094a8712510948b70008091185120a0901b20041094a8712510948b600820986128209b40082094a8712820948b500820986128209b40083094a8612830948b400820986128209b4004183098612518309b400820986128209b5004182098712518209b400820986128209b60041094a8712510948b300820986128209b70041094a8712510948b10008091186128209b80082094a8712820948af0008091187128209b80083094a8612830948ae00820987120a0901b8004183098612518309ae00820986120a0901ba004182098712518209ae00820986128209bc0041094a8712510948ad00820986128209bd0041094a8712510948ac0082098612510948bd0082094a8712820948ab0082098712510948bc0083094a8612830948aa0041094a8712820948bb004183098612518309ab0041094a8612830948bb004182098712518209ac0082094a8512518309bc0041094a8712510948ab0083094a8512518209bd0041094a8712510948aa004183098612510948bd0082094a87128209ab004182098712510948bc0083094a86128209ac0041094a87128209bc0041830986128209ad0041094a86128209bd0041820986128209ae0082098612510948bd0082098612510948ad0082098712510948bc0082098712510948ac0041094a8712820948bb0041094a87128209ad0041094a8612830948bb0041094a86128209ae0082094a8512518309bc00820986128209ae0083094a8512518209bc00820986128209ae004183098612510948bb00820986128209af004182098712510948ba00820986128209b00041094a8712820948b90082098612510948b00041094a8612830948b80082098712510948b00082098612518309b80041094a87128209b00082098712518209b90041094a86128209b00041094a8712510948b900820986128209b10041094a8712510948b800820986128209b20041094a8712820948b700820986128209b30041094a8612830948b600820986128209b40082094a8512518309b600820986128209b40083094a8512518209b600820986128209b4004183098612510948b40008091185120a0901b5004182098712510948b20008091185120a0901b70041094a8712510948b100820986128209b90041094a871251830948ae00820986128209ba0082094a871251830948ad00820986128209ba0083094a891251830948aa00820986128209ba004183098a1251830948a900820986128209bb004182098d1251830948a600820986128209bc0041094a8d1251830948a500820986128209bd004183094a8d1251830948a200820986128209be004183094a8d1251830948a00008091185120a0901c1004183094a8d12518309489c0008091185120a0901c3004183094a8d12518309489a0008820986128209c7004183094a8d12518b09488c0008850986128209c8004183094a8d12518b09488a000885091186128209cb004183094a9512518c09118b128209cc004183094a9512518a09118c128209cf004183094aaa128209d0004183094aa8120a0901d3004183094aa0120a850901d5004183094a9e120a850901d900418b094a8e120a850901df00418b094a8c120a850901eb00418e0901f100418c0901ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00ff00c8009f00200007409c00470777743000128233454095005783776655567682664095005784777435551222850011108f00478377741088000244428f00578377738900157775108e00678377608900268277208e00578377208900268277408e00378377108900168277518e00078277748a00038277738e00028277618a0001577776108d00038277308b00354344208600011185001367741095002311850013677510940001321085001577751094000151860015777510940003518600157776209400025186002682771094000273111310830017777620950067555720830026777510950047766640830015777510950037533330830015777510950026200020830015776310950005100011830013665310950003100015830013566496000520002610820004665310950004533357508200135764108600128e00027666777182001357763085000275108e006782777382001367773185001775108e0007827774820003677751850077758f000482777482000167776284000777758c00011100048277748200038277518400827775108b0026662007827775820024827741830005827775108a0001827771278277740001378277628300478377308b0033777447827772000147827764100003847783001189000784777000013665777630001583777082000245408800038477308200012067774100158377108200157751880001578377108300004777510014827773830027776289001383778400004777620002577730830027777520002082000383000157777384000047775182001221840016827764344320002573108200357771840000577631890067827766676545677751820001375084000057742089000257877773830015850000577587002083000182233433445677418900005774108500046510940000377520850026751094000016774285002777311093000005775410840027777553109200000477763084000682777510920000038277418500678277318900408800000367777185000226777530870004718800000267777386000267777311830082011137771087000001577772860002678277555382115575558277755086008200677762860001578477555786777086000001576640860001578c772085000182006322870001578b777486001082004182001182218300038b7776208600018200211123456764108200047555887762208800830014837776308300011135558577628a008300016782777630870017777666228b00840016777666308700016422208c0085003653319800a000a0000b0f2009160c09180b2408301a3222302c2a2e202d1427"

# pico-8 map format
# first 4096 bytes -> gfx (shared w/ map)
# second 4096 bytes -> map
if len(s)>=2*8192:
    raise Exception('Data string too long ({})'.format(len(s)))

tmp=s[:8192]
print("__gfx__")
# swap bytes
gfx_data = ""
for i in range(0,len(tmp),2):
    gfx_data = gfx_data + tmp[i+1:i+2] + tmp[i:i+1]
print(re.sub("(.{128})", "\\1\n", gfx_data, 0, re.DOTALL))

map_data=s[8192:]
if len(map_data)>0:
    print("__map__")
    print(re.sub("(.{256})", "\\1\n", map_data, 0, re.DOTALL))

