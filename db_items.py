from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Level, Base, Course, User


engine = create_engine('postgresql://catalog:catalog@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User = User(name="Arvind Rathee", email="arvindrathee1996@gmail.com",)
session.add(User)
session.commit()

# Levels
beginner = Level(user_id=1, name="Beginner")
session.add(beginner)
session.commit()

intermediate = Level(user_id=1, name="Intermediate")
session.add(intermediate)
session.commit()

advanced = Level(user_id=1, name="Advanced")
session.add(advanced)
session.commit()

# courses for Beginner

course = Course(
    user_id=1,
    name="An Introduction to Interactive Programming in Python (Part 1)",
    description="""This two-part course is designed to help students with very little or no computing background learn the basics of building simple interactive applications. Our language of choice, Python, is an easy-to learn, high-level computer language that is used in many of the computational courses offered on Coursera. To make learning Python easy, we have developed a new browser-based programming environment that makes developing interactive applications in Python simple. These applications will involve windows whose contents are graphical and respond to buttons, the keyboard and the mouse.""",
    review="2973",
    link="https://www.class-central.com/mooc/408/coursera-an-introduction-to-interactive-programming-in-python-part-1",
    provider="Rice University via Coursera",
    level=beginner)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Programming for Everybody (Getting Started with Python)",
    description="""This course aims to teach everyone the basics of programming computers using Python. We cover the basics of how one constructs a program from a series of simple instructions in Python. The course has no pre-requisites and avoids all but the simplest mathematics. Anyone with moderate computer experience should be able to master the materials in this course. This course will cover Chapters 1-5 of the textbook “Python for Everybody”. Once a student completes this course, they will be ready to take more advanced programming courses. This course covers Python 3. """,
    review="1602",
    link="https://www.class-central.com/mooc/4319/coursera-programming-for-everybody-getting-started-with-python",
    provider="University of Michigan via Coursera",
    level=beginner)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Introduction to Computer Science and Programming Using Python",
    description="""This course is the first of a two-course sequence: Introduction to Computer Science and Programming Using Python, and Introduction to Computational Thinking and Data Science. Together, they are designed to help people with no prior exposure to computer science or programming learn to think computationally and write programs to tackle useful problems. Some of the people taking the two courses will use them as a stepping stone to more advanced computer science courses, but for many it will be their first and last computer science courses. This run features updated lecture videos, lecture exercises, and problem sets to use the new version of Python 3.5. Even if you took the course with Python 2.7, you will be able to easily transition to Python 3.5 in future courses, or enroll now to refresh your learning. """,
    review="110",
    link="https://www.class-central.com/mooc/1341/edx-introduction-to-computer-science-and-programming-using-python",
    provider="Massachusetts Institute of Technology via edX",
    level=beginner)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Intro to Computer Science",
    description="""In this introduction to computer programming course, you’ll learn and practice key computer science concepts by building your own versions of popular web applications. You’ll learn Python, a powerful, easy-to-learn, and widely used programming language, and you’ll explore computer science basics, as you build your own search engine and social network.""",
    review="65",
    link="https://www.class-central.com/mooc/320/udacity-intro-to-computer-science",
    provider="University of Virginia via Udacity",
    level=beginner)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="An Introduction to Interactive Programming in Python (Part 2)",
    description="""This two-part course is designed to help students with very little or no computing background learn the basics of building simple interactive applications. Our language of choice, Python, is an easy-to learn, high-level computer language that is used in many of the computational courses offered on Coursera. To make learning Python easy, we have developed a new browser-based programming environment that makes developing interactive applications in Python simple. These applications will involve windows whose contents are graphical and respond to buttons, the keyboard and the mouse.""",
    review="52",
    link="https://www.class-central.com/mooc/3196/coursera-an-introduction-to-interactive-programming-in-python-part-2",
    provider="Rice University via Coursera",
    level=beginner)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Introduction to Linux",
    description="""Develop a good working knowledge of Linux using both the graphical interface and command line, covering the major Linux distribution families. Linux powers 94% of the world’s supercomputers, most of the servers powering the Internet, the majority of financial trades worldwide and a billion Android devices. In short, Linux is everywhere. It appears in many different architectures, from mainframes to server to desktop to mobile and on a staggeringly wide variety of hardware. Moreover, 97 percent of hiring managers reported that they will prioritize hiring Linux talent relative to other skills areas in the next six months, and 44 percent of hiring managers saying they’re more likely to hire a candidate with Linux certification. This course explores the various tools and techniques commonly used by Linux system administrators and end users to achieve their day-to-day work in a Linux environment. It is designed for experienced computer users who have limited or no previous exposure to Linux, whether they are working in an individual or Enterprise environment.""",
    review="37",
    link="https://www.class-central.com/mooc/1857/edx-introduction-to-linux",
    provider="Linux Foundation via edX",
    level=beginner)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Internet History, Technology, and Security",
    description="""The impact of technology and networks on our lives, culture, and society continues to increase. The very fact that you can take this course from anywhere in the world requires a technological infrastructure that was designed, engineered, and built over the past sixty years. To function in an information-centric world, we need to understand the workings of network technology. This course will open up the Internet and show you how it was created, who created it and how it works. Along the way we will meet many of the innovators who developed the Internet and Web technologies that we use today. """,
    review="35",
    link="https://www.class-central.com/mooc/335/coursera-internet-history-technology-and-security",
    provider="University of Michigan via Coursera",
    level=beginner)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Intro to HTML and CSS",
    description="""HTML and CSS are markup languages and the building blocks that make up the web. This course is called "Not your Typical Intro" because it does not follow the usual pattern of other courses and tutorials that you find on the Internet. Usually HTML and CSS are taught with a focus on language syntax. But knowing syntax alone does not enable you to create a webpage from a design. You need to know where to start and how to approach the task, in other words - you need to learn how to think like a front-end developer. """,
    review="27",
    link="https://www.class-central.com/mooc/2659/udacity-intro-to-html-and-css",
    provider="via Udacity",
    level=beginner)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Programming for the Web with JavaScript",
    description="""JavaScript is the programming language of the World Wide Web. As a professional web software developer, you will not only need to know how to program in this simple yet powerful language, but you will need to understand the fundamentals of how data is exchanged on the World Wide Web (WWW) and what tools and frameworks are available to you for creating robust, interactive web applications.""",
    review="0",
    link="https://www.class-central.com/mooc/8518/edx-programming-for-the-web-with-javascript",
    provider="University of Pennsylvania via edX",
    level=beginner)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Intro to Java Programming",
    description="""In this introductory course, you'll learn and practice essential computer science concepts using the Java programming language. You'll learn about Object Oriented Programming, a technique that allows you to use code written by other programmers in your own programs. You'll put your new Java programming skills to the test by solving real-world problems faced by software engineers.""",
    review="23",
    link="https://www.class-central.com/mooc/831/udacity-intro-to-java-programming",
    provider="San Jose State University via Udacity",
    level=beginner)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="HTML, CSS and JavaScript",
    description="""This course will teach you the essential elements of web page development, covering HTML, CSS and JavaScript. No previous experience of these technologies is necessary, although it is helpful if you have some prior programming experience. First, HTML together with CSS are discussed and explored. Then we move on to consider the essential components of JavaScript, including variables, arrays, loops, events and functions. Then we explore more advanced elements of JavaScript control, including advanced use of functions, event control, array processing, and DOM manipulation.""",
    review="20",
    link="https://www.class-central.com/mooc/4239/coursera-html-css-and-javascript",
    provider="The Hong Kong University of Science and Technology via Coursera",
    level=beginner)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="DB: Introduction to Databases",
    description='''"Introduction to Databases" was one of Stanford's inaugural three massive open online courses in the fall of 2011 and was offered again in early 2013. January 2014 will mark its third offering. The course includes video lectures and demos with in-video quizzes to check understanding, in-depth standalone quizzes, a wide variety of automatically-checked interactive programming exercises, midterm and final exams, a discussion forum, optional additional exercises with solutions, and pointers to readings and resources. Taught by Professor Jennifer Widom, the curriculum draws from Stanford's popular Introduction to Databases course.''',
    review="11",
    link="https://www.class-central.com/mooc/1580/stanford-openedx-db-introduction-to-databases",
    provider="Stanford University via Stanford OpenEdx",
    level=beginner)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Networking: Introduction to Computer Networking",
    description="""This is an introductory course on computer networking, specifically the Internet. It focuses on explaining how the Internet works, ranging from how bits are modulated on wires and in wireless to application-level protocols like BitTorrent and HTTP. It also explains the principles of how to design networks and network protocols. Students gain experience reading and understanding RFCs (Internet protocol specifications) as statements of what a system should do. The course grounds many of the concepts in current practice and recent developments, such as net neutrality and DNS security.""",
    review="10",
    link="https://www.class-central.com/mooc/1578/stanford-openedx-networking-introduction-to-computer-networking",
    provider="Stanford University via Stanford OpenEdx",
    level=beginner)
session.add(course)
session.commit()

# courses for Intermediate

course = Course(
    user_id=1,
    name="Python Data Structures",
    description="""This course will introduce the core data structures of the Python programming language. We will move past the basics of procedural programming and explore how we can use the Python built-in data structures such as lists, dictionaries, and tuples to perform increasingly complex data analysis. This course will cover Chapters 6-10 of the textbook “Python for Everybody”. This course covers Python 3. """,
    review="978",
    link="https://www.class-central.com/mooc/4174/coursera-python-data-structures",
    provider="University of Michigan via Coursera",
    level=intermediate)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Using Python to Access Web Data",
    description="""This course will show how one can treat the Internet as a source of data. We will scrape, parse, and read web data as well as access data using web APIs. We will work with HTML, XML, and JSON data formats in Python. This course will cover Chapters 11-13 of the textbook “Python for Everybody”. To succeed in this course, you should be familiar with the material covered in Chapters 1-10 of the textbook and the first two courses in this specialization. These topics include variables and expressions, conditional execution (loops, branching, and try/except), functions, Python data structures (strings, lists, dictionaries, and tuples), and manipulating files. This course covers Python 3. """,
    review="587",
    link="https://www.class-central.com/mooc/4343/coursera-using-python-to-access-web-data",
    provider="University of Michigan via Coursera",
    level=intermediate)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Using Databases with Python",
    description="""This course will introduce students to the basics of the Structured Query Language (SQL) as well as basic database design for storing data as part of a multi-step data gathering, analysis, and processing effort. The course will use SQLite3 as its database. We will also build web crawlers and multi-step data gathering and visualization processes. We will use the D3.js library to do basic data visualization. This course will cover Chapters 14-15 of the book “Python for Everybody”. To succeed in this course, you should be familiar with the material covered in Chapters 1-13 of the textbook and the first three courses in this specialization. This course covers Python 3. """,
    review="532",
    link="https://www.class-central.com/mooc/4272/coursera-using-databases-with-python",
    provider="University of Michigan via Coursera",
    level=intermediate)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Machine Learning",
    description="""Machine learning is the science of getting computers to act without being explicitly programmed. In the past decade, machine learning has given us self-driving cars, practical speech recognition, effective web search, and a vastly improved understanding of the human genome. Machine learning is so pervasive today that you probably use it dozens of times a day without knowing it. Many researchers also think it is the best way to make progress towards human-level AI. In this class, you will learn about the most effective machine learning techniques, and gain practice implementing them and getting them to work for yourself. More importantly, you'll learn about not only the theoretical underpinnings of learning, but also gain the practical know-how needed to quickly and powerfully apply these techniques to new problems. Finally, you'll learn about some of Silicon Valley's best practices in innovation as it pertains to machine learning and AI.""",
    review="313",
    link="https://www.class-central.com/mooc/835/coursera-machine-learning",
    provider="Stanford University via Coursera",
    level=intermediate)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Algorithms, Part I",
    description="""This course covers the essential information that every serious programmer needs to know about algorithms and data structures, with emphasis on applications and scientific performance analysis of Java implementations. Part I covers elementary data structures, sorting, and searching algorithms. Part II focuses on graph- and string-processing algorithms. """,
    review="55",
    link="https://www.class-central.com/mooc/339/coursera-algorithms-part-i",
    provider="Princeton University via Coursera",
    level=intermediate)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Cryptography I",
    description="""Cryptography is an indispensable tool for protecting information in computer systems. In this course you will learn the inner workings of cryptographic systems and how to correctly use them in real-world applications. The course begins with a detailed discussion of how two parties who have a shared secret key can communicate securely when a powerful adversary eavesdrops and tampers with traffic. We will examine many deployed protocols and analyze mistakes in existing systems. The second half of the course discusses public-key techniques that let two parties generate a shared secret key. Throughout the course participants will be exposed to many exciting open problems in the field and work on fun (optional) programming projects. In a second course (Crypto II) we will cover more advanced cryptographic tasks such as zero-knowledge, privacy mechanisms, and other forms of encryption. """,
    review="49",
    link="https://www.class-central.com/mooc/616/coursera-cryptography-i",
    provider="Stanford University via Coursera",
    level=intermediate)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Principles of Computing (Part 1)",
    description="""This two-part course builds upon the programming skills that you learned in our Introduction to Interactive Programming in Python course. We will augment those skills with both important programming practices and critical mathematical problem solving skills. These skills underlie larger scale computational problem solving and programming. The main focus of the class will be programming weekly mini-projects in Python that build upon the mathematical and programming principles that are taught in the class. To keep the class fun and engaging, many of the projects will involve working with strategy-based games.""",
    review="28",
    link="https://www.class-central.com/mooc/1724/coursera-principles-of-computing-part-1",
    provider="Rice University via Coursera",
    level=intermediate)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Software Testing Management",
    description="""There is much more to software testing than just finding defects. Successful software and quality assurance engineers need to also manage the testing of software.  In this course, part of the Software Testing and Verification MicroMasters program, you will learn about the management aspects of software testing. You will learn how to successfully plan, schedule, estimate and document a software testing plan.""",
    review="0",
    link="https://www.class-central.com/mooc/8171/edx-software-testing-management",
    provider="University System of Maryland via edX",
    level=intermediate)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Software Security ",
    description="""This course we will explore the foundations of software security. We will consider important software vulnerabilities and attacks that exploit them -- such as buffer overflows, SQL injection, and session hijacking -- and we will consider defenses that prevent or mitigate these attacks, including advanced testing and program analysis techniques. Importantly, we take a "build security in" mentality, considering techniques at each phase of the development cycle that can be used to strengthen the security of software systems. Successful learners in this course typically have completed sophomore/junior-level undergraduate work in a technical field, have some familiarity with programming, ideally in C/C++ and one other "managed" program language (like ML or Java), and have prior exposure to algorithms. Students not familiar with these languages but with others can improve their skills through online web tutorials. """,
    review="22",
    link="https://www.class-central.com/mooc/1728/coursera-software-security",
    provider="University of Maryland, College Park via Coursera",
    level=intermediate)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Programming Languages, Part A",
    description="""This course is an introduction to the basic concepts of programming languages, with a strong emphasis on functional programming. The course uses the languages ML, Racket, and Ruby as vehicles for teaching the concepts, but the real intent is to teach enough about how any language “fits together” to make you more effective programming in any language -- and in learning new ones. This course is neither particularly theoretical nor just about programming specifics -- it will give you a framework for understanding how to use language constructs effectively and how to design correct and elegant programs. By using different languages, you will learn to think more deeply than in terms of the particular syntax of one language. The emphasis on functional programming is essential for learning how to write robust, reusable, composable, and elegant programs. Indeed, many of the most important ideas in modern languages have their roots in functional programming. Get ready to learn a fresh and beautiful way to look at software and how to have fun building it.""",
    review="21",
    link="https://www.class-central.com/mooc/452/coursera-programming-languages-part-a",
    provider="University of Washington via Coursera",
    level=intermediate)
session.add(course)
session.commit()

# courses for Advanced

course = Course(
    user_id=1,
    name="Deep Learning",
    description="""**Machine learning** is one of the fastest-growing and most exciting fields out there, and **deep learning** represents its true bleeding edge. In this course, you’ll develop a clear understanding of the motivation for deep learning, and design intelligent systems that learn from complex and/or large-scale datasets. We’ll show you how to train and optimize basic neural networks, convolutional neural networks, and long short term memory networks. Complete learning systems in TensorFlow will be introduced via projects and assignments. You will learn to solve new classes of problems that were once thought prohibitively challenging, and come to better appreciate the complex nature of human intelligence as you solve these same problems effortlessly using deep learning methods. We have developed this course with Vincent Vanhoucke, Principal Scientist at Google, and technical lead in the Google Brain team.""",
    review="31",
    link="https://www.class-central.com/mooc/5681/udacity-deep-learning",
    provider="Google via Udacity",
    level=advanced)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Neural Networks for Machine Learning",
    description="""Learn about artificial neural networks and how they're being used for machine learning, as applied to speech and object recognition, image segmentation, modeling language and human motion, etc. We'll emphasize both the basic algorithms and the practical tricks needed to get them to work well.""",
    review="20",
    link="https://www.class-central.com/mooc/398/coursera-neural-networks-for-machine-learning",
    provider="University of Toronto via Coursera",
    level=advanced)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Bitcoin and Cryptocurrency Technologies",
    description="""To really understand what is special about Bitcoin, we need to understand how it works at a technical level. We’ll address the important questions about Bitcoin, such as: How does Bitcoin work? What makes Bitcoin different? How secure are your Bitcoins? How anonymous are Bitcoin users? What determines the price of Bitcoins? Can cryptocurrencies be regulated? What might the future hold?""",
    review="15",
    link="https://www.class-central.com/mooc/3655/coursera-bitcoin-and-cryptocurrency-technologies",
    provider="Princeton University via Coursera",
    level=advanced)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Machine Learning for Data Science and Analytics",
    description="""Machine Learning is a growing field that is used when searching the web, placing ads, credit scoring, stock trading and for many other applications. This data science course is an introduction to machine learning and algorithms. You will develop a basic understanding of the principles of machine learning and derive practical solutions using predictive analytics. We will also examine why algorithms play an essential role in Big Data analysis.""",
    review="15",
    link="https://www.class-central.com/mooc/4912/edx-machine-learning-for-data-science-and-analytics",
    provider="Columbia University via edX",
    level=advanced)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Machine Learning for Trading",
    description="""This course introduces students to the real world challenges of implementing machine learning based trading strategies including the algorithmic steps from information gathering to market orders. The focus is on how to apply probabilistic machine learning approaches to trading decisions. We consider statistical approaches like linear regression, KNN and regression trees and how to apply them to actual stock trading situations.""",
    review="13",
    link="https://www.class-central.com/mooc/1026/udacity-machine-learning-for-trading",
    provider="Georgia Institute of Technology via Udacity",
    level=advanced)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Intro to Parallel Programming",
    description="""Learn the fundamentals of parallel computing with the GPU and the CUDA programming environment! In this class, you'll learn about parallel programming by coding a series of image processing algorithms, such as you might find in Photoshop or Instagram. You'll be able to program and run your assignments on high-end GPUs, even if you don't own one yourself. """,
    review="6",
    link="https://www.class-central.com/mooc/549/udacity-intro-to-parallel-programming",
    provider="Nvidia via Udacity",
    level=advanced)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Deep Learning For Coders, Part 1",
    description="""This 7-week course is designed for anyone with at least a year of coding experience, and some memory of high-school math. You will start with step one—learning how to get a GPU server online suitable for deep learning—and go all the way through to creating state of the art, highly practical, models for computer vision, natural language processing, and recommendation systems. There are around 20 hours of lessons, and you should plan to spend around 10 hours a week for 7 weeks to complete the material. The course is based on lessons recorded during the first certificate course at The Data Institute at USF. Part 2 will be taught at the Data Institute from Feb 27, 2017, and will be available online around May 2017.""",
    review="5",
    link="https://www.class-central.com/mooc/7887/practical-deep-learning-for-coders-part-1",
    provider="fast.ai via Independent",
    level=advanced)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Applied Cryptography",
    description="""Cryptography is present in everyday life, from paying with a credit card to using the telephone. Learn all about making and breaking puzzles in computing.""",
    review="5",
    link="https://www.class-central.com/mooc/326/udacity-applied-cryptography",
    provider="University of Virginia via Udacity",
    level=advanced)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Computability, Complexity & Algorithms",
    description="""In this course, we will ask the big questions, “What is a computer? What are the limits of computation? Are there problems that no computer will ever solve? Are there problems that can’t be solved quickly? What kinds of problems can we solve efficiently and how do we go about developing these algorithms?” Understanding the power and limitations of algorithms helps us develop the tools to make real-world computers smarter, faster and safer.""",
    review="1",
    link="https://www.class-central.com/mooc/1024/udacity-computability-complexity-algorithms",
    provider="Georgia Institute of Technology via Udacity",
    level=advanced)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Learn TensorFlow and deep learning, without a Ph.D.",
    description="""Deep learning (aka neural networks) is a popular approach to building machine-learning models that is capturing developer imagination. If you want to acquire deep-learning skills but lack the time, I feel your pain. In university, I had a math teacher who would yell at me, “Mr. Görner, integrals are taught in kindergarten!” I get the same feeling today, when I read most free online resources dedicated to deep learning. My kindergarten education was apparently severely lacking in “dropout lullabies,” “cross-entropy riddles,” and “relu-gru-rnn-lstm monster stories.” Yet, these fundamental concepts are taken for granted by many, if not most, authors of online educational resources about deep learning.""",
    review="1",
    link="https://www.class-central.com/mooc/8480/learn-tensorflow-and-deep-learning-without-a-ph-d",
    provider="Google via Independent",
    level=advanced)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Intro to Information Security",
    description="""This course provides a one-semester overview of information security. It is designed to help students with prior computer and programming knowledge — both undergraduate and graduate — understand this important priority in society today. The technical content of the course gives a broad overview of essential concepts and methods for providing and evaluating security in information processing systems (operating systems and applications, networks, protocols, and so on). """,
    review="1",
    link="https://www.class-central.com/mooc/3420/udacity-intro-to-information-security",
    provider="Georgia Institute of Technology via Udacity",
    level=advanced)
session.add(course)
session.commit()

course = Course(
    user_id=1,
    name="Machine Learning 1—Supervised Learning",
    description="""This is the first course in the 3-course Machine Learning Series and is offered at Georgia Tech as CS7641. Please note that this is first course is different in structure compared to most Udacity CS courses. There is a final project at the end of the course, and there are no programming quizzes throughout this course. This course covers Supervised Learning, a machine learning task that makes it possible for your phone to recognize your voice, your email to filter spam, and for computers to learn a bunch of other cool stuff. Supervised Learning is an important component of all kinds of technologies, from stopping credit card fraud, to finding faces in camera images, to recognizing spoken language. Our goal is to give you the skills that you need to understand these technologies and interpret their output, which is important for solving a range of data science problems. And for surviving a robot uprising.""",
    review="1",
    link="https://www.class-central.com/mooc/1847/udacity-machine-learning-1-supervised-learning",
    provider="Brown University via Udacity",
    level=advanced)
session.add(course)
session.commit()
