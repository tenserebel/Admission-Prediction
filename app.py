import pywebio
from pywebio import start_server, config
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import pickle

with open('model.pkl',"rb") as f:
       model=pickle.load(f) 

config(title="My application")
config (theme="dark")
def pred():
       put_text("ADMISSION PREDICTION").style('color: #80aaff; font-size: 35px;margin: auto;width: 50%;padding: 10px;')
       info = input_group("Data",[
              input('Input your GRE SCORE：', name='gre',type=FLOAT,placeholder="Enter the GRE Score",required=True),
              input('Input your TOEFL SCORE：', name='toefl', type=FLOAT,placeholder="Enter the TOEFL Score",required=True),
              #input('Input your University Rating：', name='uni_rate', type=FLOAT,placeholder="Enter the University Rating Score",required=True),
              slider("Input your University Rating：",name='uni_rate',value=1,min_value=1, max_value=5,required=True),
              input('Input your Statement of purpose Score：', name='sop', type=FLOAT,placeholder="Enter the Statement of purpose Score",required=True),
              input('Input your Letter of Recommendation score：', name='lor', type=FLOAT,placeholder="Enter the Letter of Recommendation Score",required=True),
              input('Input your CGPA：', name='CGPA', type=FLOAT,placeholder="Enter the CGPA Score",required=True),
              #input('Input your Research Experience:', name='RE', type=FLOAT,placeholder="Enter the Research Experience: Score",required=True),
              radio("DO you have Research Experience:",name='RE', options=['Yes','No'],required=True)
              
       ])
       if info['RE']=='Yes':
              info['RE']=1
       if info['RE']=='No':
              info['RE']=0
       output=model.predict([[info['gre'], info['toefl'], info['uni_rate'], info['sop'], info['lor'], info['CGPA'], info['RE']]])[0]*100
       with use_scope('scope1'):
              put_text("Results",'Your chances of getting into UCLA are:').style('color: #ffa64d; font-size: 25px;margin: auto;width: 50%;padding: 10px;border: 3px red;')
              put_text(f"{round(output,2)}%").style('color: #ffa64d; font-size: 25px;margin: auto;width: 50%;padding: 10px;border: 3px red;')

if __name__ == '__main__':
    start_server(pred, port=8080, debug=True)
