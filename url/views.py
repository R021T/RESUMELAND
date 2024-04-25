from django.shortcuts import redirect, render
from .models import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from PIL import Image,ImageDraw,ImageFont
import io
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Create your views here.
log=0
uid=0

genai.configure(api_key=os.getenv('API_KEY'))
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config)
convo = model.start_chat(history=[])

def signin(request):
    global log
    if log==1:
        return redirect('home')
    return render(request,'login.html')

def enter(request):
    global log,uid
    if log==1:
        return redirect('home')
    username=request.GET['username']
    password=request.GET['password']
    if User.objects.filter(username=username).exists():
        user=User.objects.get(username=username)
        if password==user.password:
            log=1
            uid=user.id
            return redirect('home')
        else:
            error="Invalid password"
            return render(request,'error.html',{'error':error})
    else:
        error="Invalid username"
        return render(request,'error.html',{'error':error})

def signup(request):
    global log
    if log==1:
        return redirect('home')
    return render(request,'register.html')

def submit(request):
    global log,uid
    if log==1:
        return redirect('home')
    name=request.POST['name']
    if name is None:
        error="Enter your name"
        return render(request,'error.html',{'response':error})
    role=request.POST['role']
    if role is None:
        error="Enter your role"
        return render(request,'error.html',{'response':error})
    if request.method=='POST' and request.FILES['dp']:
        dp=request.FILES['dp']
        if dp is None:
            error="Upload your photo"
            return render(request,'error.html',{'response':error})
    phone=request.POST['phone']
    if phone is None:
        error="Enter your phone no."
        return render(request,'error.html',{'response':error})
    email=request.POST['email']
    if email is None:
        error="Enter your email"
        return render(request,'error.html',{'response':error})
    district=request.POST['district']
    if district is None:
        error="Enter your district"
        return render(request,'error.html',{'response':error})
    state=request.POST['state']
    if state is None:
        error="Enter your state"
        return render(request,'error.html',{'response':error})
    link=request.POST['link']
    if link is None:
        error="Enter your social media link"
        return render(request,'error.html',{'response':error})
    profile=request.POST['profile']
    if profile is None:
        error="Enter your summary"
        return render(request,'error.html',{'response':error})
    recent_edu=request.POST['recent_edu']
    if recent_edu is None:
        error="Enter your most recent qualification"
        return render(request,'error.html',{'response':error})
    recent_clg=request.POST['recent_clg']
    if recent_clg is None:
        error="Enter your most recent college"
        return render(request,'error.html',{'response':error})
    recent_start=request.POST['recent_start']
    if recent_start is None:
        error="Enter duration of most recent qualification"
        return render(request,'error.html',{'response':error})
    recent_stop=request.POST['recent_stop']
    recent_cgpa=request.POST['recent_cgpa']
    if recent_cgpa is None:
        error="Enter your most recent CGPA"
        return render(request,'error.html',{'response':error})
    s_recent_edu=request.POST['s_recent_edu']
    if s_recent_edu is None:
        error="Enter your second recent qualification"
        return render(request,'error.html',{'response':error})
    s_recent_clg=request.POST['s_recent_clg']
    if s_recent_clg is None:
        error="Enter your second recent college"
        return render(request,'error.html',{'response':error})
    s_recent_start=request.POST['s_recent_start']
    s_recent_stop=request.POST['s_recent_stop']
    if s_recent_start is None or s_recent_stop is None:
        error="Enter duration of second recent qualification"
        return render(request,'error.html',{'response':error})
    s_recent_per=request.POST['s_recent_per']
    if s_recent_per is None:
        error="Enter second recent percentage"
        return render(request,'error.html',{'response':error})
    t_recent_edu=request.POST['t_recent_edu']
    if t_recent_edu is None:
        error="Enter your third recent qualification"
        return render(request,'error.html',{'response':error})
    t_recent_clg=request.POST['t_recent_clg']
    if t_recent_clg is None:
        error="Enter your third recent college"
        return render(request,'error.html',{'response':error})
    t_recent_start=request.POST['t_recent_start']
    t_recent_stop=request.POST['t_recent_stop']
    if t_recent_start is None or t_recent_stop is None:
        error="Enter duration of third recent qualification"
        return render(request,'error.html',{'response':error})
    t_recent_per=request.POST['t_recent_per']
    if t_recent_per is None:
        error="Enter third recent percentage"
        return render(request,'error.html',{'response':error})
    tech=request.POST['tech']
    if tech is None:
        error="Enter your technical skills"
        return render(request,'error.html',{'response':error})
    soft=request.POST['soft']
    if soft is None:
        error="Enter your soft skills"
        return render(request,'error.html',{'response':error})
    job1=request.POST['job1']
    if job1 is None:
        error="Enter your job title"
        return render(request,'error.html',{'response':error})
    comp1=request.POST['comp1']
    if comp1 is None:
        error="Enter your company"
        return render(request,'error.html',{'response':error})
    dur1_start=request.POST['dur1_start']
    if dur1_start is None:
        error="Enter duration of job"
        return render(request,'error.html',{'response':error})
    dur1_stop=request.POST['dur1_stop']
    mod1=request.POST['mod1']
    if mod1 is None:
        error="Enter your job mode"
        return render(request,'error.html',{'response':error})
    jd1=request.POST['jd1']
    if jd1 is None:
        error="Enter your job description"
        return render(request,'error.html',{'response':error})
    jt1=request.POST['jt1']
    if jt1 is None:
        error="Enter technology used in job"
        return render(request,'error.html',{'response':error})
    job2=request.POST['job2']
    if job2 is not None:
        comp2=request.POST['comp2']
        if comp2 is None:
            error="Enter your company"
            return render(request,'error.html',{'response':error})
        dur2_start=request.POST['dur2_start']
        dur2_stop=request.POST['dur2_stop']
        if dur2_start is None or dur2_stop is None:
            error="Enter duration of job"
            return render(request,'error.html',{'response':error})
        mod2=request.POST['mod2']
        if mod2 is None:
            error="Enter your job mode"
            return render(request,'error.html',{'response':error})
        jd2=request.POST['jd2']
        if jd2 is None:
            error="Enter your job description"
            return render(request,'error.html',{'response':error})
        jt2=request.POST['jt2']
        if jt2 is None:
            error="Enter technology used in job"
            return render(request,'error.html',{'response':error})
        job3=request.POST['job3']
        if job3 is not None:
            comp3=request.POST['comp3']
            if comp3 is None:
                error="Enter your company"
                return render(request,'error.html',{'response':error})
            dur3_start=request.POST['dur3_start']
            dur3_stop=request.POST['dur3_stop']
            if dur3_start is None or dur3_stop is None:
                error="Enter duration of job"
                return render(request,'error.html',{'response':error})
            mod3=request.POST['mod3']
            if mod3 is None:
                error="Enter your job mode"
                return render(request,'error.html',{'response':error})
            jd3=request.POST['jd3']
            if jd3 is None:
                error="Enter your job description"
                return render(request,'error.html',{'response':error})
            jt3=request.POST['jt3']
            if jt3 is None:
                error="Enter technology used in job"
                return render(request,'error.html',{'response':error})
            job4=request.POST['job4']
            if job4 is not None:
                comp4=request.POST['comp4']
                if comp4 is None:
                    error="Enter your company"
                    return render(request,'error.html',{'response':error})
                dur4_start=request.POST['dur4_start']
                dur4_stop=request.POST['dur4_stop']
                if dur4_start is None or dur4_stop is None:
                    error="Enter duration of job"
                    return render(request,'error.html',{'response':error})
                mod4=request.POST['mod4']
                if mod4 is None:
                    error="Enter your job mode"
                    return render(request,'error.html',{'response':error})
                jd4=request.POST['jd4']
                if jd4 is None:
                    error="Enter your job description"
                    return render(request,'error.html',{'response':error})
                jt4=request.POST['jt4']
                if jt4 is None:
                    error="Enter technology used in job"
                    return render(request,'error.html',{'response':error})
                job5=request.POST['job5']
                if job5 is not None:
                    comp5=request.POST['comp5']
                    if comp5 is None:
                        error="Enter your company"
                        return render(request,'error.html',{'response':error})
                    dur5_start=request.POST['dur5_start']
                    dur5_stop=request.POST['dur5_stop']
                    if dur5_start is None or dur5_stop is None:
                        error="Enter duration of job"
                        return render(request,'error.html',{'response':error})
                    mod5=request.POST['mod5']
                    if mod5 is None:
                        error="Enter your job mode"
                        return render(request,'error.html',{'response':error})
                    jd5=request.POST['jd5']
                    if jd5 is None:
                        error="Enter your job description"
                        return render(request,'error.html',{'response':error})
                    jt5=request.POST['jt5']
                    if jt5 is None:
                        error="Enter technology used in job"
                        return render(request,'error.html',{'response':error})
    pro1=request.POST['pro1']
    if pro1 is None:
        error="Enter your project name"
        return render(request,'error.html',{'response':error})
    pro1_start=request.POST['pro1_start']
    pro1_stop=request.POST['pro1_stop']
    if pro1_start is None or pro1_stop is None:
        error="Enter duration of project"
        return render(request,'error.html',{'response':error})
    pro1_desc=request.POST['pro1_desc']
    if pro1_desc is None:
        error="Enter your project description"
        return render(request,'error.html',{'response':error})
    pro1_tech=request.POST['pro1_tech']
    if pro1_tech is None:
        error="Enter technology used in project"
        return render(request,'error.html',{'response':error})
    pro2=request.POST['pro2']
    if pro2 is not None:
        pro2_start=request.POST['pro2_start']
        pro2_stop=request.POST['pro2_stop']
        if pro2_start is None or pro2_stop is None:
            error="Enter duration of project"
            return render(request,'error.html',{'response':error})
        pro2_desc=request.POST['pro2_desc']
        if pro2_desc is None:
            error="Enter your project description"
            return render(request,'error.html',{'response':error})
        pro2_tech=request.POST['pro2_tech']
        if pro2_tech is None:
            error="Enter technology used in project"
            return render(request,'error.html',{'response':error})
        pro3=request.POST['pro3']
        if pro3 is not None:
            pro3_start=request.POST['pro3_start']
            pro3_stop=request.POST['pro3_stop']
            if pro3_start is None or pro3_stop is None:
                error="Enter duration of project"
                return render(request,'error.html',{'response':error})
            pro3_desc=request.POST['pro3_desc']
            if pro3_desc is None:
                error="Enter your project description"
                return render(request,'error.html',{'response':error})
            pro3_tech=request.POST['pro3_tech']
            if pro3_tech is None:
                error="Enter technology used in project"
                return render(request,'error.html',{'response':error})
            pro4=request.POST['pro4']
            if pro4 is not None:
                pro4_start=request.POST['pro4_start']
                pro4_stop=request.POST['pro4_stop']
                if pro4_start is None or pro4_stop is None:
                    error="Enter duration of project"
                    return render(request,'error.html',{'response':error})
                pro4_desc=request.POST['pro4_desc']
                if pro4_desc is None:
                    error="Enter your project description"
                    return render(request,'error.html',{'response':error})
                pro4_tech=request.POST['pro4_tech']
                if pro4_tech is None:
                    error="Enter technology used in project"
                    return render(request,'error.html',{'response':error})
                pro5=request.POST['pro5']
                if pro5 is not None:
                    pro5_start=request.POST['pro5_start']
                    pro5_stop=request.POST['pro5_stop']
                    if pro5_start is None or pro5_stop is None:
                        error="Enter duration of project"
                        return render(request,'error.html',{'response':error})
                    pro5_desc=request.POST['pro5_desc']
                    if pro5_desc is None:
                        error="Enter your project description"
                        return render(request,'error.html',{'response':error})
                    pro5_tech=request.POST['pro5_tech']
                    if pro5_tech is None:
                        error="Enter technology used in project"
                        return render(request,'error.html',{'response':error})
    c1=request.POST['c1']
    if c1 is None:
        error="Enter name of certificate"
        return render(request,'error.html',{'response':error})
    c2=request.POST['c2']
    if c2 is not None:
        c3=request.POST['c3']
        if c3 is not None:
            c4=request.POST['c4']
            if c4 is not None:
                c5=request.POST['c5']
                if c5 is not None:
                    c6=request.POST['c6']
                    if c6 is not None:
                        c7=request.POST['c7']
                        if c7 is not None:
                            c8=request.POST['c8']
                            if c8 is not None:
                                c9=request.POST['c9']
                                if c9 is not None:
                                    c10=request.POST['c10']
    username=request.POST['username']
    if username is None:
        error="Enter username"
        return render(request,'error.html',{'response':error})
    password=request.POST['password']
    if password is None:
        error="Enter password"
        return render(request,'error.html',{'response':error})
    
    if User.objects.filter(username=username).exists():
        error="Username already taken"
        return render(request,'error.html',{'response':error})
    else:
        user=User(
            name=name,
            role=role,
            photo=dp,
            phone=phone,
            email=email,
            district=district,
            state=state,
            social=link,
            summary=profile,
            username=username,
            password=password
        )
        user.save()
        education=Education(
            uid=user,
            qualification1=recent_edu,
            college1=recent_clg,
            start1=recent_start,
            stop1=recent_stop,
            score1=recent_cgpa,
            qualification2=s_recent_edu,
            college2=s_recent_clg,
            start2=s_recent_start,
            stop2=s_recent_stop,
            score2=s_recent_per,
            qualification3=t_recent_edu,
            college3=t_recent_clg,
            start3=t_recent_start,
            stop3=t_recent_stop,
            score3=t_recent_per
        )
        education.save()
        skill=Skill(
            uid=user,
            technical=tech,
            soft=soft
        )
        skill.save()
        experience=Experience(
            uid=user,
            job1=job1,
            company1=comp1,
            start1=dur1_start,
            stop1=dur1_stop,
            mode1=mod1,
            desc1=jd1,
            tech1=jt1,
            job2=job2,
            company2=comp2,
            start2=dur2_start,
            stop2=dur2_stop,
            mode2=mod2,
            desc2=jd2,
            tech2=jt2,
            job3=job3,
            company3=comp3,
            start3=dur3_start,
            stop3=dur3_stop,
            mode3=mod3,
            desc3=jd3,
            tech3=jt3,
            job4=job4,
            company4=comp4,
            start4=dur4_start,
            stop4=dur4_stop,
            mode4=mod4,
            desc4=jd4,
            tech4=jt4,
            job5=job5,
            company5=comp5,
            start5=dur5_start,
            stop5=dur5_stop,
            mode5=mod5,
            desc5=jd5,
            tech5=jt5
        )
        experience.save()
        project=Project(
            uid=user,
            project1=pro1,
            start1=pro1_start,
            stop1=pro1_stop,
            desc1=pro1_desc,
            tech1=pro1_tech,
            project2=pro2,
            start2=pro2_start,
            stop2=pro2_stop,
            desc2=pro2_desc,
            tech2=pro2_tech,
            project3=pro3,
            start3=pro3_start,
            stop3=pro3_stop,
            desc3=pro3_desc,
            tech3=pro3_tech,
            project4=pro4,
            start4=pro4_start,
            stop4=pro4_stop,
            desc4=pro4_desc,
            tech4=pro4_tech,
            project5=pro5,
            start5=pro5_start,
            stop5=pro5_stop,
            desc5=pro5_desc,
            tech5=pro5_tech
        )
        project.save()
        certificate=Certificate(
            uid=user,
            certificate1=c1,
            certificate2=c2,
            certificate3=c3,
            certificate4=c4,
            certificate5=c5,
            certificate6=c6,
            certificate7=c7,
            certificate8=c8,
            certificate9=c9,
            certificate10=c10
        )
        
        log=1
        uid=user.id
        return redirect('home')

def home(request):
    global log,uid
    if log==1:
        name=Job.objects.values_list('name', flat=True)
        return render(request,'home.html',{'response':name,'uid':uid})
    else:
        error="Unauthorized access"
        return render(request,'error.html',{'error':error})

def add(request):
    global log,uid
    try:
        if log==1:
            desc=[]
            name=request.GET['name']
            url=request.GET['url']
            
            chrome_options = Options()
            chrome_options.add_argument('--headless') 
            driver = webdriver.Chrome(options=chrome_options)


            driver.get(url)

            header = driver.find_element(By.XPATH,"/html/body/main/section[1]/div/section[2]/div/div[1]/div/h1")
            desc.append(header.text)

            SearchElement = driver.find_element(By.XPATH,'/html/body/main/section[1]/div/div')
            ClickButton  = SearchElement.find_element(By.TAG_NAME, 'button').click()
            driver.implicitly_wait(2)
            ListItems = SearchElement.find_elements(By.CSS_SELECTOR,'ul li')

            for Item in ListItems:
                desc.append(Item.text)

            driver.quit()
            user=User.objects.get(id=uid)
            job=Job(uid=user,name=name,url=url,desc=desc)
            
            image=Image.open('media/default/resume.png')
            draw=ImageDraw.Draw(image)
            font=ImageFont.truetype('arial.ttf',100)
            
            text=user.name.upper()
            position=(100,60)
            color=(0,0,0)
            draw.text(position,text=text,fill=color,font=font)
            
            text=user.role.upper()
            position=(100,180)
            font=ImageFont.truetype('arial.ttf',40)
            draw.text(position,text=text,fill=color,font=font)
            
            text=f'+91 {user.phone}'
            position=(150,345)
            font=ImageFont.truetype('arial.ttf',25)
            draw.text(position,text=text,fill=color,font=font)
            
            text=user.email
            if len(text)>30:
                up=text[:30]
                position=(150,405)
                draw.text(position,text=up,fill=color,font=font)
                down=text[30:]
                position=(150,430)
                draw.text(position,text=down,fill=color,font=font)
            else:
                position=(150,405)
                draw.text(position,text=text,fill=color,font=font)
            
            text=f'{user.district}, {user.state}'
            position=(150,470)
            draw.text(position,text=text,fill=color,font=font)
            
            text=user.social
            if len(text)>30:
                up=text[:30]
                position=(150,535)
                draw.text(position,text=up,fill=color,font=font)
                down=text[30:]
                position=(150,565)
                draw.text(position,text=down,fill=color,font=font)
            else:
                position=(150,535)
                draw.text(position,text=text,fill=color,font=font)

            convo.send_message(f'Modify the summary {user.summary} into a proper resume profile summary required for the job description {job.desc} in exactly 21 words. Do not change the summary drastically. Do not use technical terms and names of programming languages. Do not mention years of experience. Let it be simple and to the point. Do not add any * or boldening.')
            text=convo.last.text
            words=text.split()
            line1=' '.join(words[:8])
            position=(600,440)
            draw.text(position,text=line1,fill=color,font=font)
            line2=' '.join(words[8:16])
            position=(600,480)
            draw.text(position,text=line2,fill=color,font=font)
            line3=' '.join(words[16:])
            position=(600,520)
            draw.text(position,text=line3,fill=color,font=font)

            tech=Skill.objects.get(uid=user)
            convo.send_message(f'From {tech.technical} select only the skills required for the jpb description {job.desc}. Return output as a string of only the skill names separated by space. Do not add any descriptions. Output should only contain the skills mentioned in {tech.technical}. Do not add skills of your own. Number of skills in the output should not exceed 10. Do not add any * or boldening.')
            text=convo.last.text
            skills=text.split()
            x=100
            y=800
            for i in skills:
                position=(x,y)
                text=f'• {i}'
                draw.text(position,text=text,fill=color,font=font)
                y=y+50

            convo.send_message(f'Convert {tech.soft} into a string of only the skill names separated by space. Do not add any descriptions. Output should only contain the skills mentioned in {tech.soft}. Do not add skills of your own. Number of skills in the output should not exceed 10. Do not add any * or boldening.')
            text=convo.last.text
            skills=text.split()
            x=300
            y=800
            for i in skills:
                position=(x,y)
                text=f'• {i}'
                draw.text(position,text=text,fill=color,font=font)
                y=y+50

            exp=Experience.objects.get(uid=user)
            convo.send_message(f'Select at most 2 most relevant jobs from {exp.job1}, {exp.job2}, {exp.job3}, {exp.job4} and {exp.job5} which is related to job description {job.desc}. Ignore the job where value is None. Consider only those jobs with valid names. Give the output as a string of format job1,job2,job3,job4,job5 separated by commas without space after each comma where 1,2,3,4,5 refers to the job number taken in the exact same order as given in the prompt. Do not give name of job as output. Just mention the job number in the said format. Ignore the job number where value is None. Do not add any descriptions. Only choose from the given jobs. Do not add jobs of your own. Do not add any * or boldening.')
            text=convo.last.text
            if len(text)==0:
                error="Your experience does not match the job description"
                return render(request,'error.html',{'response':error})
            jobs=text.split(',')
            position=(600,725)
            attribute="job"+jobs[0]
            text=getattr(exp,attribute).upper()
            draw.text(position,text=text,fill=color,font=font)
            position=(600,760)
            attribute="company"+jobs[0]
            text=getattr(exp,attribute)
            draw.text(position,text=text,fill=color,font=font)
            position=(600,800)
            attribute="start"+jobs[0]
            text=getattr(exp,attribute)
            convo.send_message(f'Convert {text} to the format month year.')
            text=convo.last.text
            draw.text(position,text=text,fill=color,font=font)
            attribute="stop"+jobs[0]
            text=getattr(exp,attribute)
            if text is not None:
                position=(760,800)
                convo.send_message(f'Convert {text} to the format month year.')
                text=f'- {convo.last.text}'
                draw.text(position,text=text,fill=color,font=font)
                position=(1000,800)
                attribute="mode"+jobs[0]
                text=f'Mode: {getattr(exp,attribute)}'
                draw.text(position,text=text,fill=color,font=font)
            else:
                position=(900,800)
                attribute="mode"+jobs[0]
                text=f'Mode: {getattr(exp,attribute)}'
                draw.text(position,text=text,fill=color,font=font)
            position=(600,840)
            attribute="desc"+jobs[0]
            text=getattr(exp,attribute)
            convo.send_message(f'Convert description {text} to proper sentence in not more than 7 words. Do not add any * or boldening.')
            text=f'• {convo.last.text}'
            draw.text(position,text=text,fill=color,font=font)
            position=(600,880)
            attribute="tech"+jobs[0]
            text=getattr(exp,attribute)
            convo.send_message(f'Convert tech used {text} to proper sentence in not more than 7 words. Mention only the technology used and not the application. Do not add any * or boldening.')
            text=f'• {convo.last.text}'
            draw.text(position,text=text,fill=color,font=font)
            
            if len(jobs)>1:
                position=(600,950)
                attribute="job"+jobs[1]
                text=getattr(exp,attribute).upper()
                draw.text(position,text=text,fill=color,font=font)
                position=(600,985)
                attribute="company"+jobs[1]
                text=getattr(exp,attribute)
                draw.text(position,text=text,fill=color,font=font)
                position=(600,1025)
                attribute="start"+jobs[1]
                text=getattr(exp,attribute)
                convo.send_message(f'Convert {text} to the format month year. Do not add any * or boldening.')
                text=convo.last.text
                draw.text(position,text=text,fill=color,font=font)
                attribute="stop"+jobs[1]
                text=getattr(exp,attribute)
                position=(760,1025)
                convo.send_message(f'Convert {text} to the format month year. Do not add any * or boldening.')
                text=f'- {convo.last.text}'
                draw.text(position,text=text,fill=color,font=font)
                position=(1000,1025)
                attribute="mode"+jobs[1]
                text=f'Mode: {getattr(exp,attribute)}'
                draw.text(position,text=text,fill=color,font=font)
                position=(600,1065)
                attribute="desc"+jobs[1]
                text=getattr(exp,attribute)
                convo.send_message(f'Convert description {text} to proper sentence in not more than 8 words. Mention only the application and not the technology used. Do not add any * or boldening.')
                text=f'• {convo.last.text}'
                draw.text(position,text=text,fill=color,font=font)
                position=(600,1105)
                attribute="tech"+jobs[1]
                text=getattr(exp,attribute)
                convo.send_message(f'Convert tech used {text} to proper sentence in not more than 8 words. Mention only the technology used and not the application. Do not add any * or boldening.')
                text=f'• {convo.last.text}'
                draw.text(position,text=text,fill=color,font=font)

            pro=Project.objects.get(uid=user)
            convo.send_message(f'Select at most 2 most relevant jobs from {pro.project1}, {pro.project2}, {pro.project3}, {pro.project4} and {pro.project5} which is related to job description {job.desc}. Ignore the projects where value is None. Consider only those projects with valid names. Give the output as a string of format project1,project2,project3,project4,project5 separated by commas without space after each comma where 1,2,3,4,5 refers to the job number taken in the exact same order as given in the prompt. Do not give name of project as output. Just mention the project number in the said format. Ignore the project number where value is None. Do not add any descriptions. Only choose from the given projects. Do not add projects of your own. Do not add any * or boldening.')
            text=convo.last.text
            if len(text)==0:
                error="Your projects do not match the job description"
                return render(request,'error.html',{'response':error})
            projects=text.split(',')
            position=(600,1330)
            attribute="project"+projects[0]
            text=getattr(pro,attribute).upper()
            draw.text(position,text=text,fill=color,font=font)
            position=(600,1370)
            attribute="start"+projects[0]
            text=getattr(pro,attribute)
            convo.send_message(f'Convert {text} to the format month year. Do not add any * or boldening.')
            text=convo.last.text
            draw.text(position,text=text,fill=color,font=font)
            position=(760,1370)
            attribute="stop"+projects[0]
            text=getattr(pro,attribute)
            convo.send_message(f'Convert {text} to the format month year. Do not add any * or boldening.')
            text=f'- {convo.last.text}'
            draw.text(position,text=text,fill=color,font=font)
            position=(600,1410)
            attr1="desc"+projects[0]
            attr2="tech"+projects[0]
            text1=getattr(pro,attr1)
            text2=getattr(pro,attr2)
            convo.send_message(f'Create a proper sentence using information in {text1} and {text2} in not more than 8 words. Do not add any * or boldening.')
            text=f'• {convo.last.text}'
            draw.text(position,text=text,fill=color,font=font)

            if len(projects)>1:
                position=(600,1470)
                attribute="project"+projects[1]
                text=getattr(pro,attribute).upper()
                draw.text(position,text=text,fill=color,font=font)
                position=(600,1510)
                attribute="start"+projects[1]
                text=getattr(pro,attribute)
                convo.send_message(f'Convert {text} to the format month year. Do not add any * or boldening.')
                text=convo.last.text
                draw.text(position,text=text,fill=color,font=font)
                position=(760,1510)
                attribute="stop"+projects[1]
                text=getattr(pro,attribute)
                convo.send_message(f'Convert {text} to the format month year. Do not add any * or boldening.')
                text=f'- {convo.last.text}'
                draw.text(position,text=text,fill=color,font=font)
                position=(600,1550)
                attr1="desc"+projects[1]
                attr2="tech"+projects[1]
                text1=getattr(pro,attr1)
                text2=getattr(pro,attr2)
                convo.send_message(f'Create a proper sentence using information in {text1} and {text2} in not more than 8 words. Do not add any * or boldening.')
                text=f'• {convo.last.text}'
                draw.text(position,text=text,fill=color,font=font)

            cer=Certificate.objects.get(uid=user)
            convo.send_message(f'Select at most 4 certificates from {cer.certificate1}, {cer.certificate2}, {cer.certificate3}, {cer.certificate4}, {cer.certificate5}, {cer.certificate6}, {cer.certificate7}, {cer.certificate8}, {cer.certificate9} and {cer.certificate10} which is relevant to job description {job.desc}. Ignore the certificates where value is None. Consider only those certificates with valid names. Output should be a string of names of certificates separated by commas without space between each comma. Do not add any descriptions. Only choose from the given certificates. Do not add certificates of your own.')
            text=convo.last.text
            certificates=text.split(',')
            x=600
            y=1760
            for i in certificates:
                position=(x,y)
                text=f'• {i}'
                draw.text(position,text=text,fill=color,font=font)
                y=y+40

            edu=Education.objects.get(uid=user)
            position=(90,1410)
            text=edu.qualification1.upper()
            draw.text(position,text=text,fill=color,font=font)
            text=edu.college1
            if len(text)>28:
                words=text.split()
                line1=' '.join(words[:5])
                position=(90,1450)
                draw.text(position,text=line1,fill=color,font=font)
                line2=' '.join(words[5:])
                position=(90,1490)
                draw.text(position,text=line2,fill=color,font=font)
                position=(90,1530)
                text=edu.start1
                draw.text(position,text=text,fill=color,font=font)
                position=(150,1530)
                if edu.stop1 is not None:
                    text=f'- {edu.stop1}'
                else:
                    text=f'- Present'
                draw.text(position,text=text,fill=color,font=font)
                position=(300,1530)
                text=f'CGPA: {edu.score1}/10'
                draw.text(position,text=text,fill=color,font=font)
                position=(90,1610)
                text=edu.qualification2.upper()
                draw.text(position,text=text,fill=color,font=font)
                text=edu.college2
                if len(text)>28:
                    words=text.split()
                    line1=' '.join(words[:5])
                    position=(90,1650)
                    draw.text(position,text=line1,fill=color,font=font)
                    line2=' '.join(words[5:])
                    position=(90,1690)
                    draw.text(position,text=line2,fill=color,font=font)
                    position=(90,1730)
                    text1=edu.start2
                    text2=edu.stop2
                    text=f'{text1} - {text2}'
                    draw.text(position,text=text,fill=color,font=font)
                    position=(300,1730)
                    text=f'Percentage: {edu.score2}%'
                    draw.text(position,text=text,fill=color,font=font)
                    position=(90,1810)
                    text=edu.qualification3
                    draw.text(position,text=text,fill=color,font=font)
                    text=edu.college3
                    if len(text)>28:
                        words=text.split()
                        line1=' '.join(words[:5])
                        position=(90,1850)
                        draw.text(position,text=line1,fill=color,font=font)
                        line2=' '.join(words[5:])
                        position=(90,1890)
                        draw.text(position,text=line2,fill=color,font=font)
                        position=(90,1930)
                        text1=edu.start3
                        text2=edu.stop3
                        text=f'{text1} - {text2}'
                        draw.text(position,text=text,fill=color,font=font)
                        position=(300,1930)
                        text=f'Percentage: {edu.score3}%'
                        draw.text(position,text=text,fill=color,font=font)
                    else:
                        position=(90,1850)
                        draw.text(position,text=text,fill=color,font=font)
                        position=(90,1890)
                        text1=edu.start3
                        text2=edu.stop3
                        text=f'{text1} - {text2}'
                        draw.text(position,text=text,fill=color,font=font)
                        position=(300,1890)
                        text=f'Percentage: {edu.score3}%'
                        draw.text(position,text=text,fill=color,font=font)
                else:
                    position=(90,1650)
                    draw.text(position,text=text,fill=color,font=font)
                    position=(90,1690)
                    text1=edu.start2
                    text2=edu.stop2
                    text=f'{text1} - {text2}'
                    draw.text(position,text=text,fill=color,font=font)
                    position=(300,1690)
                    text=f'Percentage: {edu.score2}%'
                    draw.text(position,text=text,fill=color,font=font)
                    position=(90,1770)
                    text=edu.qualification3
                    draw.text(position,text=text,fill=color,font=font)
                    text=edu.college3
                    if len(text)>28:
                        words=text.split()
                        line1=' '.join(words[:5])
                        position=(90,1810)
                        draw.text(position,text=line1,fill=color,font=font)
                        line2=' '.join(words[5:])
                        position=(90,1850)
                        draw.text(position,text=line2,fill=color,font=font)
                        position=(90,1890)
                        text1=edu.start3
                        text2=edu.stop3
                        text=f'{text1} - {text2}'
                        draw.text(position,text=text,fill=color,font=font)
                        position=(300,1890)
                        text=f'Percentage: {edu.score3}%'
                        draw.text(position,text=text,fill=color,font=font)
                    else:
                        position=(90,1810)
                        draw.text(position,text=text,fill=color,font=font)
                        position=(90,1850)
                        text1=edu.start3
                        text2=edu.stop3
                        text=f'{text1} - {text2}'
                        draw.text(position,text=text,fill=color,font=font)
                        position=(300,1850)
                        text=f'Percentage: {edu.score3}%'
                        draw.text(position,text=text,fill=color,font=font)
            else:
                position=(90,1450)
                draw.text(position,text=text,fill=color,font=font)
                position=(90,1490)
                text=edu.start1
                draw.text(position,text=text,fill=color,font=font)
                position=(150,1490)
                if edu.stop1 is not None:
                    text=f'- {edu.stop1}'
                else:
                    text='- Present'
                draw.text(position,text=text,fill=color,font=font)
                position=(400,1490)
                text=f'CGPA: {edu.score1}/10'
                draw.text(position,text=text,fill=color,font=font)
                position=(90,1570)
                text=edu.qualification2.upper()
                draw.text(position,text=text,fill=color,font=font)
                text=edu.college2
                if len(text)>28:
                    words=text.split()
                    line1=' '.join(words[:5])
                    position=(90,1610)
                    draw.text(position,text=line1,fill=color,font=font)
                    line2=' '.join(words[5:])
                    position=(90,1650)
                    draw.text(position,text=line2,fill=color,font=font)
                    position=(90,1690)
                    text1=edu.start2
                    text2=edu.stop2
                    text=f'{text1} - {text2}'
                    draw.text(position,text=text,fill=color,font=font)
                    position=(300,1690)
                    text=f'Percentage: {edu.score2}%'
                    draw.text(position,text=text,fill=color,font=font)
                    position=(90,1770)
                    text=edu.qualification3
                    draw.text(position,text=text,fill=color,font=font)
                    text=edu.college3
                    if len(text)>28:
                        words=text.split()
                        line1=' '.join(words[:5])
                        position=(90,1810)
                        draw.text(position,text=line1,fill=color,font=font)
                        line2=' '.join(words[5:])
                        position=(90,1850)
                        draw.text(position,text=line2,fill=color,font=font)
                        position=(90,1890)
                        text1=edu.start3
                        text2=edu.stop3
                        text=f'{text1} - {text2}'
                        draw.text(position,text=text,fill=color,font=font)
                        position=(300,1890)
                        text=f'Percentage: {edu.score3}%'
                        draw.text(position,text=text,fill=color,font=font)
                    else:
                        position=(90,1810)
                        draw.text(position,text=text,fill=color,font=font)
                        position=(90,1850)
                        text1=edu.start3
                        text2=edu.stop3
                        text=f'{text1} - {text2}'
                        draw.text(position,text=text,fill=color,font=font)
                        position=(300,1850)
                        text=f'Percentage: {edu.score3}%'
                        draw.text(position,text=text,fill=color,font=font)
                else:
                    position=(90,1610)
                    draw.text(position,text=text,fill=color,font=font)
                    position=(90,1650)
                    text1=edu.start2
                    text2=edu.stop2
                    text=f'{text1} - {text2}'
                    draw.text(position,text=text,fill=color,font=font)
                    position=(300,1650)
                    text=f'Percentage: {edu.score2}%'
                    draw.text(position,text=text,fill=color,font=font)
                    position=(90,1730)
                    text=edu.qualification3
                    draw.text(position,text=text,fill=color,font=font)
                    text=edu.college3
                    if len(text)>28:
                        words=text.split()
                        line1=' '.join(words[:5])
                        position=(90,1770)
                        draw.text(position,text=line1,fill=color,font=font)
                        line2=' '.join(words[5:])
                        position=(90,1810)
                        draw.text(position,text=line2,fill=color,font=font)
                        position=(90,1850)
                        text1=edu.start3
                        text2=edu.stop3
                        text=f'{text1} - {text2}'
                        draw.text(position,text=text,fill=color,font=font)
                        position=(300,1850)
                        text=f'Percentage: {edu.score3}%'
                        draw.text(position,text=text,fill=color,font=font)
                    else:
                        position=(90,1770)
                        draw.text(position,text=text,fill=color,font=font)
                        position=(90,1810)
                        text1=edu.start3
                        text2=edu.stop3
                        text=f'{text1} - {text2}'
                        draw.text(position,text=text,fill=color,font=font)
                        position=(300,1810)
                        text=f'Percentage: {edu.score3}%'
                        draw.text(position,text=text,fill=color,font=font)
            
            dp=Image.open(f'media/{user.photo}').resize((300,400))
            width, height = dp.size
            background=Image.new("RGBA",(width,height),(255,255,255,0))
            mask=Image.new("L",dp.size,0)
            draw=ImageDraw.Draw(mask)
            draw.ellipse((0,0,300,300),fill=255)
            dp.putalpha(mask)
            background.paste(dp,(0,0),mask=dp)
            position=(1050,80)
            image.paste(background,position,mask=background)
            
            resume=io.BytesIO()
            image.save(resume, format='PNG')
            job.resume.save(f'{user.name}_{job.name}.png',resume)
            job.save()
            
            return redirect('home')
        else:
            error="Unauthorized access"
            return render(request,'error.html',{'error':error})
    except Exception as e:
        add(request)

def view(request):
    global log
    if log==1:
        job=request.GET['job']
        desc=Job.objects.filter(name=job).values_list('desc',flat=True)
        convo.send_message(f'Convert {desc} into points with heading on top. Display each point one below the other as a list. Only mention important points. Do not make it too long. Do not add any * or boldening.')
        description=convo.last.text.split('\n')
        resume=Job.objects.filter(name=job).first().resume
        return render(request,'view.html',{'response':description,'resume':resume})
    else:
        error="Unauthorized access"
        return render(request,'error.html',{'error':error})
