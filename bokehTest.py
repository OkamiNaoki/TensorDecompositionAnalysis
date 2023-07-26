import numpy as np

from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, CustomJS, Slider, Select, HoverTool
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot

import os
import numpy as np

TOOLS = "box_select,help,reset"


# Specify the path to the 'results.npy' file
results_file = os.path.join('result', 'results.npy')

# Load the data from the 'results.npy' file
a = np.load(results_file)

# Load the data from the 'c1.npy' file
c1 = np.load('c1.npy')

# Load the data from the 'c2.npy' file
c2 = np.load('c2.npy')

# Load the data from the 'c3.npy' file
c3 = np.load('c3.npy')

# Load the data from the 'c4.npy' file
c4 = np.load('c4.npy')

# Load the data from the 'tensor_0.npy' file
tensor_0 = np.load('tensor_0.npy')

# Load the data from the 'tensor_1.npy' file
tensor_1 = np.load('tensor_1.npy')

# Load the data from the 'tensor_2.npy' file
tensor_2 = np.load('tensor_2.npy')

# Load the data from the 'tensor_all.npy' file
tensor_all = np.load('tensor_all.npy')

# Load the data from the 'tensor_decomposition_b0.npy' file
b0 = [np.load(f'tensor_decomposition_b0_{i}.npy') for i in range(3)]

# Load the data from the 'tensor_decomposition_b1.npy' file
b1 = [np.load(f'tensor_decomposition_b1_{i}.npy') for i in range(3)]

# Load the data from the 'tensor_decomposition_b2.npy' file
b2 = [np.load(f'tensor_decomposition_b2_{i}.npy') for i in range(3)]

# Load the data from the 'tensor_decomposition_b3.npy' file
b3 = [np.load(f'tensor_decomposition_b3_{i}.npy') for i in range(3)]

u0 = np.load('tensor_decomposition_a0.npy')

u1 = np.load('tensor_decomposition_a1.npy')

u2 = np.load('tensor_decomposition_a2.npy')

u3 = np.load('tensor_decomposition_a3.npy')      

mem=np.load('mem.npy')     

u4=range(6)
# Create ColumnDataSource
source4 = ColumnDataSource(data={
    '0': a[0][:, 0],
    '1': a[1][:, 0],
    '2': a[2][:, 0],
    '3': a[3][:, 0],  # Fixed index from 2 to 3
    '4': a[4][:, 0],
    '5': a[5][:, 0],
    '6': a[0][:, 1],
    '7': a[1][:, 1],
    '8': a[2][:, 1],
    '9': a[3][:, 1],  # Fixed index from 2 to 3
    '10': a[4][:, 1],
    '11': a[5][:, 1],
    '12': a[0][:, 2],
    '13': a[1][:, 2],
    '14': a[2][:, 2],
    '15': a[3][:, 2],  # Fixed index from 2 to 3
    '16': a[4][:, 2],
    '17': a[5][:, 2],
    '18': a[0][:, 3],
    '19': a[1][:, 3],
    '20': a[2][:, 3],
    '21': a[3][:, 3],  # Fixed index from 2 to 3
    '22': a[4][:, 3],
    '23': a[5][:, 3]
})


# Create the ColumnDataSource with the loaded data
source5 = ColumnDataSource(data={'0': c1, '1': c2, '2': c3, '3': c4})

#u6=range(len(b0[0][:,0]))
source60 = ColumnDataSource(data={'0' : b0[0][:,0],'1' : b0[0][:,1],'2' : b0[0][:,2],'3' : b0[0][:,3]})
source61 = ColumnDataSource(data={'0' : b1[0][:,0],'1' : b1[0][:,1],'2' : b1[0][:,2],'3' : b1[0][:,3]})
source62 = ColumnDataSource(data={'0' : b2[0][:,0],'1' : b2[0][:,1],'2' : b2[0][:,2],'3' : b2[0][:,3]})
source63 = ColumnDataSource(data={'0' : b3[0][:,0],'1' : b3[0][:,1],'2' : b3[0][:,2],'3' : b3[0][:,3]})


u7=range(len(b0[1][:,0]))
source70 = ColumnDataSource(data={'0' : b0[1][:,0],'1' : b0[1][:,1],'2' : b0[1][:,2],'3' : b0[1][:,3]})
source71 = ColumnDataSource(data={'0' : b1[1][:,0],'1' : b1[1][:,1],'2' : b1[1][:,2],'3' : b1[1][:,3]})
source72 = ColumnDataSource(data={'0' : b2[1][:,0],'1' : b2[1][:,1],'2' : b2[1][:,2],'3' : b2[1][:,3]})
source73 = ColumnDataSource(data={'0' : b3[1][:,0],'1' : b3[1][:,1],'2' : b3[1][:,2],'3' : b3[1][:,3]})

u8=range(len(b0[2][:,0]))
source80 = ColumnDataSource(data={'0' : b0[2][:,0],'1' : b0[2][:,1],'2' : b0[2][:,2],'3' : b0[2][:,3]})
source81 = ColumnDataSource(data={'0' : b1[2][:,0],'1' : b1[2][:,1],'2' : b1[2][:,2],'3' : b1[2][:,3]})
source82 = ColumnDataSource(data={'0' : b2[2][:,0],'1' : b2[2][:,1],'2' : b2[2][:,2],'3' : b2[2][:,3]})
source83 = ColumnDataSource(data={'0' : b3[2][:,0],'1' : b3[2][:,1],'2' : b3[2][:,2],'3' : b3[2][:,3]})




l1=range(len(tensor_0[0,:,0]))
d1 = {str(s): tensor_0[:,s,0] for s in l1}
sourceT1=ColumnDataSource(data=d1)

d2 = {str(s): tensor_1[:,s,0] for s in l1}
sourceT2=ColumnDataSource(data=d2)

d3 = {str(s): tensor_2[:,s,0] for s in l1}
sourceT3=ColumnDataSource(data=d3)

d4 = {str(s): tensor_all[:,s,0] for s in l1}
sourceT4=ColumnDataSource(data=d4)


s1 = ColumnDataSource(data=dict(x=list(u1), y=list(u1)))
p1 = figure(width=400, height=400,title="core1", tools=TOOLS)
p1.vbar(x='x', top='y', source=s1, alpha=0.6)



s2 = ColumnDataSource(data=dict(x=list(u2), y=list(u2)))
p2 = figure(width=400, height=400,title="core2", tools=TOOLS)
p2.vbar('x', 1,'y', source=s2, alpha=0.6)

s3 = ColumnDataSource(data=dict(x=list(u3), y=list(u3)))
p3 = figure(width=400, height=400, title="core3", tools=TOOLS)
p3.vbar('x',1, 'y', source=s3, alpha=0.6)

v4=np.zeros(len(u4))
s4 = ColumnDataSource(data=dict(x=list(u4), y=v4))
p4 = figure(width=200, height=150, title="Difference", tools=TOOLS)
p4.vbar('x',1,'y', source=s4,color="#808080")

p4.axis.visible = False
p4.grid.grid_line_color = None


p4.toolbar.logo = None
p4.toolbar_location = None

s7 = ColumnDataSource(data=dict(x=mem, y=c1))
p5 = figure(x_range=mem,width=1200, height=150, title="MainCore", tools=TOOLS,
              background_fill_color="#fafafa")
p5.vbar('x',1, 'y', source=s7,color="#696969")
p5.axis.visible = False
p5.grid.grid_line_color = None
p5.toolbar.logo = None
p5.toolbar_location = None

hover_tool = HoverTool(
    tooltips=[
        ("name", '@x')
    ],
    formatters={
        "time": "datetime",

    },
    mode='vline'
)

p5.tools.append(hover_tool)

s8 = ColumnDataSource(data=dict(x=mem, y=mem))
p6 = figure(x_range=mem,width=1000, height=200, title="core", tools=TOOLS,
              background_fill_color="#fafafa")
p6.vbar('x',1, 'y', source=s8)
    
s5 = ColumnDataSource(data=dict(x=[], y=[]))
s5.data["x"].append(0)
s6 = ColumnDataSource(data=dict(x=[], y=[]))
s6.data["x"].append(0)

s5inds = ColumnDataSource(data=dict(x=[], y=[]))
s5inds.data["x"].append(0)

s9 = ColumnDataSource(data=dict(x=[], y=[]))
p9 = figure(width=200, height=90,title="FirstTensorTime", tools=TOOLS)
p9.vbar('x',1, 'y', source=s9,color="#517fe6")

p9.tools.append(hover_tool)
p9.axis.visible = False
p9.grid.grid_line_color = None

p9.toolbar.logo = None
p9.toolbar_location = None

s10 = ColumnDataSource(data=dict(x=list(u7), y=list(u7)))
p10 = figure(width=300, height=90,title="FirstTensorSpace", tools=TOOLS)
p10.vbar('x', 1,'y', source=s10,color="#93dc6f")

p10.tools.append(hover_tool)
p10.axis.visible = False
p10.grid.grid_line_color = None
p10.toolbar.logo = None
p10.toolbar_location = None

s11 = ColumnDataSource(data=dict(x=list(u8), y=list(u8)))
p11 = figure(width=200, height=90, title="FirstTensorMeasure", tools=TOOLS)
p11.vbar('x',1, 'y', source=s11,color="#f4949f")

p11.tools.append(hover_tool)
p11.axis.visible = False
p11.grid.grid_line_color = None

p11.toolbar.logo = None
p11.toolbar_location = None

s12 = ColumnDataSource(data=dict(x=[], y=[]))
p12 = figure(width=200, height=90,title="SecondTensorTime", tools=TOOLS)
p12.vbar('x',1,'y', source=s12,color="#517fe6")

p12.tools.append(hover_tool)

p12.axis.visible = False
p12.grid.grid_line_color = None
p12.toolbar.logo = None
p12.toolbar_location = None

s13 = ColumnDataSource(data=dict(x=list(u7), y=list(u7)))
p13 = figure(width=300, height=90,title="SecondTensorSpace", tools=TOOLS)
p13.vbar('x', 1,'y', source=s13,color="#93dc6f")

p13.tools.append(hover_tool)
p13.axis.visible = False
p13.grid.grid_line_color = None

p13.toolbar.logo = None
p13.toolbar_location = None

s14 = ColumnDataSource(data=dict(x=list(u8), y=list(u8)))
p14 = figure(width=200, height=90, title="SecondTensorMeasure", tools=TOOLS,background_fill_color="#fafafa")
p14.vbar('x',1, 'y', source=s14,color="#f4949f")

p14.tools.append(hover_tool)
p14.axis.visible = False
p14.grid.grid_line_color = None
p14.toolbar.logo = None
p14.toolbar_location = None

sdt = ColumnDataSource(data=dict(x=[], y=[]))
pdt = figure(width=200, height=150,title="DifferenceTensorTime", tools=TOOLS)
#pdt.vbar('x',1,'y', source=sdt,color="#1845aa")
pdt.circle('x','y', source=sdt,color="#1845aa")

pdt.tools.append(hover_tool)
pdt.axis.visible = False
pdt.grid.grid_line_color = None

pdt.toolbar.logo = None
pdt.toolbar_location = None

sds = ColumnDataSource(data=dict(x=list(u7), y=list(u7)))
pds = figure(width=300, height=150,title="DifferenceTensorSpace", tools=TOOLS)
#pds.vbar('x', 1,'y', source=sds,color="#53a22a")
pds.circle('x','y', source=sds,color="#53a22a")
pds.axis.visible = False
pds.grid.grid_line_color = None
pds.tools.append(hover_tool)
pds.toolbar.logo = None
pds.toolbar_location = None

sdm = ColumnDataSource(data=dict(x=list(u8), y=list(u8)))
pdm = figure(width=200, height=150, title="DifferenceTensorMeasure", tools=TOOLS)
pdm.vbar('x',1, 'y', source=sdm,color="#f25a6b")

pdm.tools.append(hover_tool)
pdm.axis.visible = False
pdm.grid.grid_line_color = None
pdm.toolbar.logo = None
pdm.toolbar_location = None

s15=ColumnDataSource(data=dict(time=[], space=[],measure=[]))

s16=ColumnDataSource(data=dict(time=[], space=[],measure=[]))



s9.selected.js_on_change('indices', CustomJS(args=dict(s=s9,s1=s15), code="""
        const inds = s.selected.indices;
        const d12 = s1.data;
        
        d12['time'] = [];
        for (let i = 0; i < inds.length; i++) {
            d12['time'].push(inds[i]);
        }
        console.log(s1.data['time'])
        s1.change.emit();

"""))



s10.selected.js_on_change('indices', CustomJS(args=dict(s=s10,s1=s15), code="""
        const inds = s.selected.indices;
        const d12 = s1.data;
        
        d12['space'] = [];
        for (let i = 0; i < inds.length; i++) {
            d12['space'].push(inds[i]);
        }
        console.log(s1.data['space'])
        s1.change.emit();

"""))

s11.selected.js_on_change('indices', CustomJS(args=dict(s=s11,s1=s15), code="""
        const inds = s.selected.indices;
        const d12 = s1.data;
        
        d12['measure'] = [];
        for (let i = 0; i < inds.length; i++) {
            d12['measure'].push(inds[i]);
        }
        console.log(s1.data['measure'])
        s1.change.emit();

"""))

s12.selected.js_on_change('indices', CustomJS(args=dict(s=s12,s1=s16), code="""
        const inds = s.selected.indices;
        const d12 = s1.data;
        
        d12['time'] = [];
        for (let i = 0; i < inds.length; i++) {
            d12['time'].push(inds[i]);
        }
        console.log(s1.data['time'])
        s1.change.emit();

"""))

s13.selected.js_on_change('indices', CustomJS(args=dict(s=s13,s1=s16), code="""
        const inds = s.selected.indices;
        const d12 = s1.data;
        
        d12['space'] = [];
        for (let i = 0; i < inds.length; i++) {
            d12['space'].push(inds[i]);
        }
        console.log(s1.data['space'])
        s1.change.emit();

"""))

s14.selected.js_on_change('indices', CustomJS(args=dict(s=s14,s1=s16), code="""
        const inds = s.selected.indices;
        const d12 = s1.data;
        
        d12['measure'] = [];
        for (let i = 0; i < inds.length; i++) {
            d12['measure'].push(inds[i]);
        }
        console.log(s1.data['measure'])
        s1.change.emit();

"""))

sdt.selected.js_on_change('indices', CustomJS(args=dict(s=sdt), code="""
        const inds = s.selected.indices;

        console.log(inds);

"""))

sds.selected.js_on_change('indices', CustomJS(args=dict(s=sds), code="""
        const inds = s.selected.indices;

        console.log(inds);

"""))

sdm.selected.js_on_change('indices', CustomJS(args=dict(s=sdm), code="""
        const inds = s.selected.indices;

        console.log(inds);

"""))


s7.selected.js_on_change('indices', CustomJS(args=dict(s=s7,s5inds=s5inds,s4=s4,source4=source4,m=mem,s1=s9,source60=source60,source61=source61,source62=source62,source63=source63,s2=s10,source70=source70,source71=source71,source72=source72,source73=source73,s3=s11,source80=source80,source81=source81,source82=source82,source83=source83,s5=s5,sds=sds,sdt=sdt,sdm=sdm), code="""
        const inds = s.selected.indices;
        const S5inds=s5inds.data;
        S5inds["x"][0]=inds[0];
        s5inds.change.emit();
        const d = s.data;
        console.log(parseInt(Number(m[inds[0]])/100));
        console.log(parseInt((Number(m[inds[0]])/10)%10));
        console.log(Number(m[inds[0]])%10);
        
        const A1=parseInt(Number(m[inds[0]])/100);
        const d60 = source60.data;
        const d61 = source61.data;
        const d62 = source62.data;
        const d63 = source63.data;
        
        const d12 = s1.data;
        d12['x']=[];
        d12['y'] = [];
        
        
        const ddt = sdt.data;
        ddt['x']=[];
        ddt['y'] = [];
        
        
        const A2=parseInt((Number(m[inds[0]])/10)%10);
        const d70 = source70.data;
        const d71 = source71.data;
        const d72 = source72.data;
        const d73 = source73.data;

        const d22 = s2.data;
        d22['y'] = [];
        
        const dds = sds.data;
        dds['y'] = [];
        
        const A3=parseInt(Number(m[inds[0]])%10);
        const d80 = source80.data;
        const d81 = source81.data;
        const d82 = source82.data;
        const d83 = source83.data;
        
        const d32 = s3.data;
        d32['y'] = [];
        
        const ddm = sdm.data;
        ddm['y'] = [];
        
        let q=0;
        let r=0;
        
        const S5=s5.data;
        console.log(S5['x'][0]);
        switch(S5['x'][0]){
            case 0:
                q=0;
                r=1;
                console.log(S5['x'][0]);
                for (let i = 0; i < d60[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d60[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d70[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d80[A3][i]);
                }
                for (let i = 0; i < Math.min(d60[A1].length,d61[A1].length); i++) {
                    ddt['x'].push(i);
                    ddt['y'].push(d60[A1][i]-d61[A1][i]);
                }
                for (let i = 0; i < dds['x'].length; i++) {
                    dds['y'].push(d70[A2][i]-d71[A2][i]);
                }
                for (let i = 0; i < ddm['x'].length; i++) {
                    ddm['y'].push(d80[A3][i]-d81[A3][i]);
                }
                break;
            case 1:
                q=0;
                r=2;
                for (let i = 0; i < d60[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d60[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d70[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d80[A3][i]);
                }
                for (let i = 0; i < Math.min(d60[A1].length,d62[A1].length); i++) {
                    ddt['x'].push(i);
                    ddt['y'].push(d60[A1][i]-d62[A1][i]);
                }
                for (let i = 0; i < dds['x'].length; i++) {
                    dds['y'].push(d70[A2][i]-d72[A2][i]);
                }
                for (let i = 0; i < ddm['x'].length; i++) {
                    ddm['y'].push(d80[A3][i]-d82[A3][i]);
                }
                break;
            case 2:
                q=0;
                r=3;
                for (let i = 0; i < d60[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d60[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d70[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d80[A3][i]);
                }
                for (let i = 0; i < Math.min(d60[A1].length,d63[A1].length); i++) {
                    ddt['x'].push(i);
                    ddt['y'].push(d60[A1][i]-d63[A1][i]);
                }
                for (let i = 0; i < dds['x'].length; i++) {
                    dds['y'].push(d70[A2][i]-d73[A2][i]);
                }
                for (let i = 0; i < ddm['x'].length; i++) {
                    ddm['y'].push(d80[A3][i]-d83[A3][i]);
                }
                break;
            case 3:
                q=1;
                r=2;
                for (let i = 0; i < d61[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d61[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d71[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d81[A3][i]);
                }
                for (let i = 0; i < Math.min(d61[A1].length,d62[A1].length); i++) {
                    ddt['x'].push(i);
                    ddt['y'].push(d61[A1][i]-d62[A1][i]);
                }
                for (let i = 0; i < dds['x'].length; i++) {
                    dds['y'].push(d71[A2][i]-d72[A2][i]);
                }
                for (let i = 0; i < ddm['x'].length; i++) {
                    ddm['y'].push(d81[A3][i]-d82[A3][i]);
                }
                break;
            case 4:
                q=1;
                r=3;
                for (let i = 0; i < d61[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d61[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d71[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d81[A3][i]);
                }
                for (let i = 0; i < Math.min(d61[A1].length,d63[A1].length); i++) {
                    ddt['x'].push(i);
                    ddt['y'].push(d61[A1][i]-d63[A1][i]);
                }
                for (let i = 0; i < dds['x'].length; i++) {
                    dds['y'].push(d71[A2][i]-d73[A2][i]);
                }
                for (let i = 0; i < ddm['x'].length; i++) {
                    ddm['y'].push(d81[A3][i]-d83[A3][i]);
                }
                break;
            case 5:
                q=2;
                r=3;
                for (let i = 0; i < d62[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d62[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d72[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d82[A3][i]);
                }
                for (let i = 0; i < Math.min(d62[A1].length,d63[A1].length); i++) {
                    ddt['x'].push(i);
                    ddt['y'].push(d62[A1][i]-d63[A1][i]);
                }
                for (let i = 0; i < dds['x'].length; i++) {
                    dds['y'].push(d72[A2][i]-d73[A2][i]);
                }
                for (let i = 0; i < ddm['x'].length; i++) {
                    ddm['y'].push(d82[A3][i]-d83[A3][i]);
                }
                break;
            default:
                console.log('hi');
                break;
                   
        }

        s1.change.emit();
        s2.change.emit();
        s3.change.emit();
        sds.change.emit();
        sdt.change.emit();
        sdm.change.emit();
        
        const d41=source4.data;
        const d42=s4.data;
        d42['y'][0]=0;
        d42['y'][1]=0;
        d42['y'][2]=0;
        d42['y'][3]=0;
        d42['y'][4]=0;
        d42['y'][5]=0;
        const p=6*A2;
        for (let i = 0; i < d41[p].length; i++) {
            d42['y'][0]=d42['y'][0]+d41[p][i]*d41[p][i];
            d42['y'][1]=d42['y'][1]+d41[p+1][i]*d41[p+1][i];
            d42['y'][2]=d42['y'][2]+d41[p+2][i]*d41[p+2][i];
            d42['y'][3]=d42['y'][3]+d41[p+3][i]*d41[p+3][i];
            d42['y'][4]=d42['y'][4]+d41[p+4][i]*d41[p+4][i];
            d42['y'][5]=d42['y'][5]+d41[p+5][i]*d41[p+5][i];
            
        }
        Math.sqrt(d42['y'][0]);
        Math.sqrt(d42['y'][1]);
        Math.sqrt(d42['y'][2]);
        Math.sqrt(d42['y'][3]);
        Math.sqrt(d42['y'][4]);
        Math.sqrt(d42['y'][5]);
        s4.change.emit();



"""))

s7.selected.js_on_change('indices', CustomJS(args=dict(s=s7,m=mem,s1=s12,source60=source60,source61=source61,source62=source62,source63=source63,s2=s13,source70=source70,source71=source71,source72=source72,source73=source73,s3=s14,source80=source80,source81=source81,source82=source82,source83=source83,s5=s5), code="""
        const inds = s.selected.indices;
        const d = s.data;
        console.log(parseInt(Number(m[inds[0]])/100));
        console.log(parseInt((Number(m[inds[0]])/10)%10));
        console.log(Number(m[inds[0]])%10);
        
        const A1=parseInt(Number(m[inds[0]])/100);
        const d60 = source60.data;
        const d61 = source61.data;
        const d62 = source62.data;
        const d63 = source63.data;
        
        const d12 = s1.data;
        d12['x']=[];
        d12['y'] = [];
        
        
        
        
        
        const A2=parseInt((Number(m[inds[0]])/10)%10);
        const d70 = source70.data;
        const d71 = source71.data;
        const d72 = source72.data;
        const d73 = source73.data;

        const d22 = s2.data;
        d22['y'] = [];
        
        
        
        const A3=parseInt(Number(m[inds[0]])%10);
        const d80 = source80.data;
        const d81 = source81.data;
        const d82 = source82.data;
        const d83 = source83.data;
        
        const d32 = s3.data;
        d32['y'] = [];
        
        let q=0;
        let r=0;
        
        const S5=s5.data;
        console.log(S5['x'][0]);
        switch(S5['x'][0]){
            case 0:
                q=0;
                r=1;
                console.log(S5['x'][0]);
                for (let i = 0; i < d61[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d61[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d71[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d81[A3][i]);
                }
                break;
            case 1:
                q=0;
                r=2;
                for (let i = 0; i < d62[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d62[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d72[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d82[A3][i]);
                }
                break;
            case 2:
                q=0;
                r=3;
                for (let i = 0; i < d63[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d63[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d73[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d83[A3][i]);
                }
                break;
            case 3:
                q=1;
                r=2;
                for (let i = 0; i < d62[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d62[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d72[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d82[A3][i]);
                }
                break;
            case 4:
                q=1;
                r=3;
                for (let i = 0; i < d63[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d63[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d73[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d83[A3][i]);
                }
                break;
            case 5:
                q=2;
                r=3;
                for (let i = 0; i < d63[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d63[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d73[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d83[A3][i]);
                }
                break;
            default:
                console.log('hi');
                break;
                   
        }

        s1.change.emit();
        s2.change.emit();
        s3.change.emit();
        



"""))

s3.selected.js_on_change('indices', CustomJS(args=dict(s=s3,s4=s4,s5=s5,s6=s6,source4=source4,s7=s7,source5=source5,s8=s8), code="""
        const inds = s.selected.indices;
        const d = s.data;
        const S5=s5.data;
        S5['x'][0]=inds[0];
        const S6=s6.data;
        const d41=source4.data;
        const d42=s4.data;
        const p=S5['x'][0]+6*S6['x'][0];
        for (let i = 0; i < d42['x'].length; i++) {
            if(d42['y'][i]>0){
                d42['y'][i]=d41[p][i];
            }
        }
        console.log(p);        
        s5.change.emit();
        s4.change.emit();
        
        const S7=s7.data;
        const S8=s8.data;
        const d5=source5.data;
        const q=0;
        const r=0;
        
        console.log(S5['x'][0]);
        switch(S5['x'][0]){
            case '0':
                q=0;
                r=1;
                break;
            case '1':
                q=0;
                r=2;
                break;
            case '2':
                q=0;
                r=3;
                break;
            case '3':
                q=1;
                r=2;
                break;
            case '4':
                q=1;
                r=3;
                break;
            case '5':
                q=2;
                r=3;
                break;
            default:
                break;
                   
        }
        
        for (let i = 0; i < S7['x'].length; i++) {
            S7['y'][i]=d5[q][i];
            S8['y'][i]=d5[r][i];
        }
        s7.change.emit();
        s8.change.emit();

"""))

s1.selected.js_on_change('indices', CustomJS(args=dict(s=s1,source4=source4,s4=s4,s5=s5,s6=s6), code="""
        const inds = s.selected.indices;
        const d = s.data;
        console.log(inds);
        const d41=source4.data;
        const d42=s4.data;
        const S6=s6.data;
        const S5=s5.data;
        for (let i = 0; i < d42['x'].length; i++) {
            d42['y'][i]=0;
        }
        const p=S5['x'][0]+6*S6['x'][0];
        console.log(p);
        for (let i = 0; i < inds.length; i++) {
            d42['y'][inds[i]]=d41[p][inds[i]];
            console.log(inds.length);
        }
        
        console.log(d42['y']);
        s4.change.emit();
"""))
s2.selected.js_on_change('indices', CustomJS(args=dict(s=s2,s4=s4,s5=s5,s6=s6,source4=source4), code="""
        const inds = s.selected.indices;
        const d = s.data;
        const S6=s6.data;
        S6['x'][0]=inds[0];
        const d41=source4.data;
        const d42=s4.data;
        const S5=s5.data;
        const p=S5['x'][0]+6*S6['x'][0];
        console.log(p);
        for (let i = 0; i < d42['x'].length; i++) {
            if(d42['y'][i]>0){
                d42['y'][i]=d41[p][i];
            }
        }
        console.log(S5['x'][0]);        
        s4.change.emit();
        s6.change.emit();
        
"""))

s4.selected.js_on_change('indices', CustomJS(args=dict(s=s4,s5=s5,s5inds=s5inds,source4=source4,m=mem,s1=s9,source60=source60,source61=source61,source62=source62,source63=source63,s2=s10,source70=source70,source71=source71,source72=source72,source73=source73,s3=s11,source80=source80,source81=source81,source82=source82,source83=source83,sds=sds,sdm=sdm,sdt=sdt), code="""

        const in4 = s.selected.indices;
        const S5=s5.data;
        S5['x'][0]=in4[0];
        s5.change.emit();
        
        const inds=s5inds.data;
        const d = s.data;
        console.log(parseInt(Number(m[inds['x'][0]])/100));
        console.log(parseInt((Number(m[inds['x'][0]])/10)%10));
        console.log(parseInt(Number(m[inds['x'][0]])%10));
        
        const A1=parseInt(Number(m[inds['x'][0]])/100);
        const d60 = source60.data;
        const d61 = source61.data;
        const d62 = source62.data;
        const d63 = source63.data;
        
        const d12 = s1.data;
        d12['x']=[];
        d12['y'] = [];
        
        const ddt = sdt.data;
        ddt['x']=[];
        ddt['y'] = [];
        
        
        
        const A2=parseInt((Number(m[inds['x'][0]])/10)%10);
        const d70 = source70.data;
        const d71 = source71.data;
        const d72 = source72.data;
        const d73 = source73.data;

        const d22 = s2.data;
        d22['y'] = [];
        
        const dds = sds.data;
        dds['y'] = [];
        
        
        
        const A3=parseInt(Number(m[inds['x'][0]])%10);
        const d80 = source80.data;
        const d81 = source81.data;
        const d82 = source82.data;
        const d83 = source83.data;
        
        const d32 = s3.data;
        d32['y'] = [];
        
        const ddm = sdm.data;
        ddm['y'] = [];
        
        
        let q=0;
        let r=0;
        
        console.log(S5['x'][0]);
        switch(S5['x'][0]){
            case 0:
                q=0;
                r=1;
                console.log(S5['x'][0]);
                for (let i = 0; i < d60[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d60[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d70[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d80[A3][i]);
                }
                for (let i = 0; i < dds['x'].length; i++) {
                    dds['y'].push(d70[A2][i]-d71[A2][i]);
                }
                for (let i = 0; i < Math.min(d60[A1].length,d61[A1].length); i++) {
                    ddt['x'].push(i);
                    ddt['y'].push(d60[A1][i]-d61[A1][i]);
                }
                for (let i = 0; i < ddm['x'].length; i++) {
                    ddm['y'].push(d80[A3][i]-d81[A3][i]);
                }
                break;
            case 1:
                q=0;
                r=2;
                for (let i = 0; i < d60[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d60[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d70[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d80[A3][i]);
                }
                for (let i = 0; i < dds['x'].length; i++) {
                    dds['y'].push(d70[A2][i]-d72[A2][i]);
                }
                for (let i = 0; i < Math.min(d60[A1].length,d62[A1].length); i++) {
                    ddt['x'].push(i);
                    ddt['y'].push(d60[A1][i]-d62[A1][i]);
                }
                for (let i = 0; i < ddm['x'].length; i++) {
                    ddm['y'].push(d80[A3][i]-d82[A3][i]);
                }
                break;
            case 2:
                q=0;
                r=3;
                for (let i = 0; i < d60[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d60[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d70[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d80[A3][i]);
                }
                for (let i = 0; i < dds['x'].length; i++) {
                    dds['y'].push(d70[A2][i]-d73[A2][i]);
                }
                for (let i = 0; i < Math.min(d60[A1].length,d63[A1].length); i++) {
                    ddt['x'].push(i);
                    ddt['y'].push(d60[A1][i]-d63[A1][i]);
                }
                
                for (let i = 0; i < ddm['x'].length; i++) {
                    ddm['y'].push(d80[A3][i]-d83[A3][i]);
                }
                break;
            case 3:
                q=1;
                r=2;
                for (let i = 0; i < d61[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d61[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d71[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d81[A3][i]);
                }
                for (let i = 0; i < dds['x'].length; i++) {
                    dds['y'].push(d71[A2][i]-d72[A2][i]);
                }
                for (let i = 0; i < Math.min(d61[A1].length,d62[A1].length); i++) {
                    ddt['x'].push(i);
                    ddt['y'].push(d61[A1][i]-d62[A1][i]);
                }
                for (let i = 0; i < ddm['x'].length; i++) {
                    ddm['y'].push(d81[A3][i]-d82[A3][i]);
                }
                break;
            case 4:
                q=1;
                r=3;
                for (let i = 0; i < d61[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d61[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d71[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d81[A3][i]);
                }
                for (let i = 0; i < dds['x'].length; i++) {
                    dds['y'].push(d71[A2][i]-d73[A2][i]);
                }
                for (let i = 0; i < Math.min(d61[A1].length,d63[A1].length); i++) {
                    ddt['x'].push(i);
                    ddt['y'].push(d61[A1][i]-d63[A1][i]);
                }
                for (let i = 0; i < ddm['x'].length; i++) {
                    ddm['y'].push(d81[A3][i]-d83[A3][i]);
                }
                break;
            case 5:
                q=2;
                r=3;
                for (let i = 0; i < d62[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d62[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d72[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d82[A3][i]);
                }
                for (let i = 0; i < dds['x'].length; i++) {
                    dds['y'].push(d72[A2][i]-d73[A2][i]);
                }
                for (let i = 0; i < Math.min(d62[A1].length,d63[A1].length); i++) {
                    ddt['x'].push(i);
                    ddt['y'].push(d62[A1][i]-d63[A1][i]);
                }
                
                for (let i = 0; i < ddm['x'].length; i++) {
                    ddm['y'].push(d82[A3][i]-d83[A3][i]);
                }
                break;
                
            default:
                console.log('hi');
                break;
                   
        }

        s1.change.emit();
        s2.change.emit();
        s3.change.emit();
        
        sds.change.emit();
        sdt.change.emit();
        sdm.change.emit();
"""))

s4.selected.js_on_change('indices', CustomJS(args=dict(s=s4,s5=s5,s5inds=s5inds,m=mem,s1=s12,source60=source60,source61=source61,source62=source62,source63=source63,s2=s13,source70=source70,source71=source71,source72=source72,source73=source73,s3=s14,source80=source80,source81=source81,source82=source82,source83=source83), code="""
        const in4 = s.selected.indices;
        const S5=s5.data;
        S5['x'][0]=in4[0];
        s5.change.emit();
        
        const inds = s5inds.data;
        const d = s.data;
        
        console.log('000');
        console.log(m[inds['x'][0]]);
        console.log(parseInt(Number(m[inds['x'][0]])/100));
        console.log(parseInt((Number(m[inds['x'][0]])/10)%10));
        console.log(parseInt(Number(m[inds['x'][0]])%10));
        
        const A1=parseInt(Number(m[inds['x'][0]])/100);
        const d60 = source60.data;
        const d61 = source61.data;
        const d62 = source62.data;
        const d63 = source63.data;
        
        const d12 = s1.data;
        d12['x']=[];
        d12['y'] = [];
        
        
        
        
        
        const A2=parseInt((Number(m[inds['x'][0]])/10)%10);
        const d70 = source70.data;
        const d71 = source71.data;
        const d72 = source72.data;
        const d73 = source73.data;

        const d22 = s2.data;
        d22['y'] = [];
        
        
        
        const A3=parseInt(Number(m[inds['x'][0]])%10);
        const d80 = source80.data;
        const d81 = source81.data;
        const d82 = source82.data;
        const d83 = source83.data;
        
        const d32 = s3.data;
        d32['y'] = [];
        
        let q=0;
        let r=0;
        
        console.log(S5['x'][0]);
        switch(S5['x'][0]){
            case 0:
                q=0;
                r=1;
                console.log(S5['x'][0]);
                for (let i = 0; i < d61[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d61[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d71[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d81[A3][i]);
                }
                break;
            case 1:
                q=0;
                r=2;
                for (let i = 0; i < d62[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d62[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d72[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d82[A3][i]);
                }
                break;
            case 2:
                q=0;
                r=3;
                for (let i = 0; i < d63[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d63[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d73[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d83[A3][i]);
                }
                break;
            case 3:
                q=1;
                r=2;
                for (let i = 0; i < d62[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d62[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d72[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d82[A3][i]);
                }
                break;
            case 4:
                q=1;
                r=3;
                for (let i = 0; i < d63[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d63[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d73[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d83[A3][i]);
                }
                break;
            case 5:
                q=2;
                r=3;
                for (let i = 0; i < d63[A1].length; i++) {
                    d12['x'].push(i);
                    d12['y'].push(d63[A1][i]);
                }
                for (let i = 0; i < d22['x'].length; i++) {
                    d22['y'].push(d73[A2][i]);
                }
                for (let i = 0; i < d32['x'].length; i++) {
                    d32['y'].push(d83[A3][i]);
                }
                break;
            default:
                console.log('hi');
                break;
                   
        }
        console.log('qr');
        console.log(q);
        console.log(r);
        s1.change.emit();
        s2.change.emit();
        s3.change.emit();
        



"""))

#show(gridplot([[p5,p9,p10,p11],[p4,p12,p13,p14]]))
#show(column(row(p5,p4),row(pdt,column(p9,p12),pds,column(p10,p13),pdm,column(p11,p14))))


from bokeh.io import curdoc, output_file, show
import pandas as pd  # pandasをインポート
from bokeh.transform import linear_cmap
from bokeh.palettes import Viridis256
from bokeh.models import ColumnDataSource, LinearColorMapper

# ヒートマップ用のデータを生成
data = np.random.rand(36, 24)

# インデックスとカラムの組み合わせを作成
index = np.arange(0, 36)
columns = np.arange(0, 24)
index, columns = np.meshgrid(index, columns)
index = index.flatten()
columns = columns.flatten()

# データをpandas.DataFrameに変換
df = pd.DataFrame({'index': index, 'columns': columns, 'value': data.flatten()})

# カラーマッパーを設定
color_mapper = LinearColorMapper(palette=Viridis256, low=df['value'].min(), high=df['value'].max())

# データソースをColumnDataSourceに変換
source = ColumnDataSource(df)

# ヒートマップの描画
p_heatmap = figure(width=300, height=400, x_range=(0, 24), y_range=(0, 36),title="heatmap")
p_heatmap.rect(x='columns', y='index', width=1, height=1, source=source, line_color=None,
               fill_color=linear_cmap('value', palette=Viridis256, low=df['value'].min(), high=df['value'].max()))

# カラーバーを設定
color_bar = figure(width=80, height=400, y_range=(df['value'].min(), df['value'].max()), toolbar_location=None)
color_bar.rect(x=1, y='value', width=1, height=1, source=source, line_color=None,
               fill_color=linear_cmap('value', palette=Viridis256, low=df['value'].min(), high=df['value'].max()))

p_heatmap.tools.append(hover_tool)
p_heatmap.axis.visible = False
p_heatmap.grid.grid_line_color = None

p_heatmap.toolbar.logo = None
p_heatmap.toolbar_location = None

# ヒートマップの描画
p_heatmap1 = figure(width=300, height=400, x_range=(0, 24), y_range=(0, 36),title="heatmap1")
p_heatmap1.rect(x='columns', y='index', width=1, height=1, source=source, line_color=None,
               fill_color=linear_cmap('value', palette=Viridis256, low=df['value'].min(), high=df['value'].max()))

# カラーバーを設定
color_bar1 = figure(width=80, height=400, y_range=(df['value'].min(), df['value'].max()), toolbar_location=None)
color_bar1.rect(x=1, y='value', width=1, height=1, source=source, line_color=None,
               fill_color=linear_cmap('value', palette=Viridis256, low=df['value'].min(), high=df['value'].max()))

p_heatmap1.tools.append(hover_tool)
p_heatmap1.axis.visible = False
p_heatmap1.grid.grid_line_color = None

p_heatmap1.toolbar.logo = None
p_heatmap1.toolbar_location = None

# ヒートマップの描画
p_heatmap2 = figure(width=300, height=400, x_range=(0, 24), y_range=(0, 36),title="heatmap2")
p_heatmap2.rect(x='columns', y='index', width=1, height=1, source=source, line_color=None,
               fill_color=linear_cmap('value', palette=Viridis256, low=df['value'].min(), high=df['value'].max()))

# カラーバーを設定
color_bar2 = figure(width=80, height=400, y_range=(df['value'].min(), df['value'].max()), toolbar_location=None)
color_bar2.rect(x=1, y='value', width=1, height=1, source=source, line_color=None,
               fill_color=linear_cmap('value', palette=Viridis256, low=df['value'].min(), high=df['value'].max()))

p_heatmap2.tools.append(hover_tool)
p_heatmap2.axis.visible = False
p_heatmap2.grid.grid_line_color = None

p_heatmap2.toolbar.logo = None
p_heatmap2.toolbar_location = None
# レイアウトを作成
layout = column(row(p5, p4), row(pdt, column(p9, p12), pds, column(p10, p13), pdm, column(p11, p14)), row(p_heatmap,p_heatmap1,p_heatmap2))

# レイアウトをドキュメントに追加
curdoc().add_root(layout)