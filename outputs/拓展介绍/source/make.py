import os, sys
B = os.path.dirname(os.path.abspath(__file__))
have = set(os.listdir(os.path.join(B, 'img')))

def img(*cands):
    for c in cands:
        if c in have:
            return 'img/' + c
    raise SystemExit('no image for %s' % (cands,))

# 优先用场景对应的新图，没有就用已有图兜底
P_COVER = img('3.jpg')
P_ABOUT = img('2.jpg')
P_KIDS = img('k.jpg', '1.jpg')
P_GOV = img('5.jpg')
P_CAMP = img('z.jpg', '3.jpg')
P_ADV = img('d.jpg', '4.jpg')
P_CASE_GOV = img('p.jpg', '5.jpg')
P_END = img('2.jpg')
WALL = [x for x in ['k.jpg', 'p.jpg', '2.jpg', '3.jpg', 'd.jpg', '5.jpg', '4.jpg', 'z.jpg', '1.jpg'] if x in have]
CAP = {
    'k.jpg': '幼儿园亲子运动会', 'p.jpg': '残联公益文体活动', '2.jpg': '教职工团建拓展',
    '3.jpg': '团队协作 · 巨球竞速', 'd.jpg': '社区共建趣味运动会', '5.jpg': '社区党建主题活动',
    '4.jpg': '元旦主题嘉年华', 'z.jpg': '青少年趣味挑战', '1.jpg': '室内团队协作项目',
}

def footer(n):
    return f'<div class="foot"><span>湖南绿猴体育发展有限公司</span><span>{n:02d}</span></div>'

def head(no, cn, en):
    return f'<div class="hd"><div class="no">{no}</div><div><h2>{cn}</h2><div class="en">{en}</div></div></div>'

pages = []

# 1 封面
pages.append(f'''
<section class="page cover">
  <img class="bg" src="{P_COVER}">
  <div class="shade"></div>
  <div class="cv">
    <div class="tag">合作推介材料 · 2026</div>
    <h1>湖南绿猴体育<br>发展有限公司</h1>
    <div class="sub">团建拓展 · 趣味运动会 · 亲子运动会 · 职工子女托管</div>
    <div class="line"></div>
    <div class="slogan">把复杂的执行交给我们，把精彩的瞬间留给客户</div>
  </div>
  <div class="since">SINCE 2010</div>
</section>''')

# 2 公司概况
pages.append(f'''
<section class="page">
  {head('01', '公司概况', 'COMPANY PROFILE')}
  <div class="about">
    <div class="atext">
      <p class="lead">十六载深耕，定义文体新高度</p>
      <p>湖南绿猴体育发展有限公司成立于 2010 年，是湖南省内资深的<b>幼儿体育与综合文体活动方案提供商</b>。</p>
      <p>我们不只做活动策划，更通过“运动 + 文化”的系统化解决方案，为客户创造深度连接。十六年来累计服务数千家机构，已成为行业内极具影响力的文体发展平台。</p>
      <div class="stats">
        <div><b>2010</b><span>公司成立</span></div>
        <div><b>16<i>年</i></b><span>行业沉淀</span></div>
        <div><b>数千<i>家</i></b><span>累计服务机构</span></div>
      </div>
      <div class="creed"><span>专业驱动</span><span>创意引领</span><span>安全第一</span></div>
    </div>
    <div class="aimg"><img src="{P_ABOUT}"></div>
  </div>
  {footer(2)}
</section>''')

# 3 业务总览
pages.append(f'''
<section class="page">
  {head('02', '三大核心业务', 'CORE BUSINESS')}
  <div class="biz3">
    <div class="bz"><img src="{P_KIDS}"><div class="bt"><em>A</em><h3>幼儿体育与亲子活动</h3><p>幼儿园场景 · 亲子运动会 · 幼儿体能体系</p></div></div>
    <div class="bz"><img src="{P_GOV}"><div class="bt"><em>B</em><h3>政企定制文体活动</h3><p>趣味运动会 · 团建拓展 · 节庆与文化日 · 政务公益</p></div></div>
    <div class="bz"><img src="{P_CAMP}"><div class="bt"><em>C</em><h3>职工子女定制托管</h3><p>工会 / HR 福利采购 · 寒暑假托管 · 主题营</p></div></div>
  </div>
  {footer(3)}
</section>''')

# 4 业务A
pages.append(f'''
<section class="page">
  {head('A', '幼儿体育与亲子活动', 'KINDERGARTEN & FAMILY')}
  <div class="split">
    <div class="simg"><img src="{P_KIDS}"></div>
    <div class="stext">
      <p class="intro">针对学龄前儿童身心发育特点，提供<b>从策划到执行的全案服务</b>。</p>
      <div class="item"><h4>大型亲子运动会</h4><p>结合情景化的主题设计，让家长和孩子一起动起来——强化家园共育，同时提升幼儿园品牌形象。</p></div>
      <div class="item"><h4>幼儿体能体系搭建 <small>可选服务</small></h4><p>科学评估幼儿体能现状，定制化课程指导，把运动从“一次活动”变成“日常体系”。</p></div>
      <div class="fit">适合：公办 / 民办幼儿园、早教机构、教育主管部门</div>
    </div>
  </div>
  {footer(4)}
</section>''')

# 5 业务B
pages.append(f'''
<section class="page">
  {head('B', '政企定制文体活动', 'GOVERNMENT & ENTERPRISE')}
  <div class="split rev">
    <div class="stext">
      <p class="intro">把<b>企业文化 / 政务目标</b>深度植入体育活动，让活动有主题、有记忆点。</p>
      <div class="grid2">
        <div class="item"><h4>趣味运动会 · 团建拓展</h4><p>提升员工凝聚力，打破部门壁垒。</p></div>
        <div class="item"><h4>主题节庆活动</h4><p>三八、五四、六一、中秋、元旦等重要节点的创意文体策划。</p></div>
        <div class="item"><h4>企业文化日</h4><p>根据品牌调性，定制专属的主题文化日。</p></div>
        <div class="item"><h4>政务 / 公益活动承办</h4><p>符合政府标准的规范流程与安全保障方案。</p></div>
      </div>
      <div class="fit">适合：机关单位、企事业单位、工会、街道社区、党群组织</div>
    </div>
    <div class="simg"><img src="{P_GOV}"></div>
  </div>
  {footer(5)}
</section>''')

# 6 业务C
pages.append(f'''
<section class="page">
  {head('C', '政企职工子女定制托管', 'CHILDCARE FOR EMPLOYEES')}
  <p class="intro wide">面向市直机关、企事业单位，推出<b>职工子女寒暑假定制化托管服务</b>，解决职工假期的育儿后顾之忧——这是工会 / HR 可直接采购的员工福利。</p>
  <div class="five">
    <div><b>01</b><h4>安全托管</h4></div>
    <div><b>02</b><h4>学业辅导</h4></div>
    <div><b>03</b><h4>营养餐食</h4></div>
    <div><b>04</b><h4>兴趣培养</h4></div>
    <div><b>05</b><h4>生活照顾</h4></div>
  </div>
  <div class="cbot">
    <div class="item"><h4>多元化场景</h4><p>从幼儿的启蒙课程，到学龄儿童的学业辅导，全年龄段覆盖。</p></div>
    <div class="item"><h4>主题夏 / 冬令营</h4><p>结合运动与拓展，打造专属“欢乐营”，让孩子独立应对挑战、收获成长。</p></div>
    <div class="cimg"><img src="{P_CAMP}"></div>
  </div>
  {footer(6)}
</section>''')

# 7 优势
pages.append(f'''
<section class="page dark">
  {head('03', '为什么选择绿猴', 'WHY US')}
  <div class="adv">
    <div class="ad"><div class="k">16<i>年</i></div><h4>行业沉淀</h4><p>历经十六年市场检验，积累了海量执行方案库，能应对各种复杂场地与多变需求。</p></div>
    <div class="ad"><div class="k">SOP</div><h4>标准化执行流程</h4><p>从前期调研、方案构思到现场应急预案，一套成熟的 SOP 体系，确保“零差错”交付。</p></div>
    <div class="ad"><div class="k">定制</div><h4>跨界整合 · 全案定制</h4><p>拒绝同质化。根据客户行业背景（消防、残联、医疗科技等）深度开发内容，让活动有独特的“灵魂”。</p></div>
  </div>
  <div class="advimg"><img src="{P_ADV}"></div>
  {footer(7)}
</section>''')

# 8 流程
steps = [('需求沟通', '了解单位目标、人数、场地与预算'), ('前期调研', '实地勘察场地，评估风险点'),
         ('方案构思', '主题创意 + 项目编排 + 流程设计'), ('方案确认', '与客户逐项确认，按需调整'),
         ('筹备落地', '物料、器材、人员、应急预案就位'), ('现场执行', '专业团队控场，安全全程保障'),
         ('总结交付', '活动影像与总结材料交付')]
st = ''.join(f'<div class="st"><div class="dot">{i+1}</div><h4>{a}</h4><p>{b}</p></div>' for i, (a, b) in enumerate(steps))
pages.append(f'''
<section class="page">
  {head('04', '标准化服务流程', 'SERVICE PROCESS')}
  <p class="intro wide">每一场活动都按同一套 SOP 推进，<b>客户只需要提需求、做确认</b>，其余交给我们。</p>
  <div class="steps">{st}</div>
  <div class="safe">
    <div><h4>安全第一</h4><p>每场活动配备现场应急预案</p></div>
    <div><h4>专业控场</h4><p>专人主持、专人裁判、专人保障</p></div>
    <div><h4>全案负责</h4><p>策划到执行一个团队对接到底</p></div>
  </div>
  {footer(8)}
</section>''')

# 9 案例
pages.append(f'''
<section class="page">
  {head('05', '标杆案例与口碑', 'SELECTED CLIENTS')}
  <p class="intro wide">长期服务于对活动标准要求极高的<b>政府部门与头部企业</b>，积累了深厚的信任背书。</p>
  <div class="cases">
    <div class="cs"><span class="ty">政务标杆</span><h3>长沙市残联</h3><p>展现人文关怀与组织温度的专项公益活动。</p></div>
    <div class="cs"><span class="ty">政务标杆</span><h3>长沙市岳麓区<br>消防救援支队</h3><p>结合专业属性的高标准联合演训 / 文体活动。</p></div>
    <div class="cs"><span class="ty">企业标杆</span><h3>三诺生物<br><small>Sinocare</small></h3><p>企业文化深度定制，通过文体活动助力品牌凝聚力提升。</p></div>
  </div>
  <div class="trust">政府部门 · 公益组织 · 上市企业 · 幼儿园 · 街道社区 —— 不同类型的客户，同一套高标准交付。</div>
  {footer(9)}
</section>''')

# 10 图片墙
n = len(WALL)
cells = ''.join(f'<figure><img src="img/{x}"><figcaption>{CAP[x]}</figcaption></figure>' for x in WALL)
pages.append(f'''
<section class="page">
  {head('06', '活动现场', 'ON SITE')}
  <div class="wall w{n}">{cells}</div>
  {footer(10)}
</section>''')

# 11 合作
pages.append(f'''
<section class="page cover end">
  <img class="bg" src="{P_END}">
  <div class="shade"></div>
  <div class="cv">
    <div class="tag">合作共赢</div>
    <h1 class="q">把复杂的执行交给我们，<br>把精彩的瞬间留给客户。</h1>
    <div class="sub">湖南绿猴体育发展有限公司，期待与贵单位携手，<br>共同打造具有深度影响力与感染力的文体盛宴。</div>
    <div class="contact">
      <div><span>联系人</span><i></i></div>
      <div><span>电　话</span><i></i></div>
      <div><span>微　信</span><i></i></div>
    </div>
  </div>
</section>''')

css = open(os.path.join(B, 'style.css'), encoding='utf-8').read()
html = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>湖南绿猴体育 合作推介</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700;900&family=Noto+Serif+SC:wght@700;900&display=swap" rel="stylesheet">
<style>{css}</style></head><body>{''.join(pages)}</body></html>'''
open(os.path.join(B, 'deck.html'), 'w', encoding='utf-8').write(html)
print('pages', len(pages), 'wall', WALL)
