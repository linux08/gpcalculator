



def main():
            name= raw_input("enter the name of the student'and press enter\n'>>>")
            matricno = raw_input("pls enter the matric no'and press enter\n'>>")
            n = eval(raw_input("pls enter how many subject'and press enter\n'>>"))
            b =raw_input("work with grade(g) or score(s) by typing g for grade or s for score>>>\n")
            tsum = 0
            asum = 0
            alist =[]
            blist =[]
            clist = []
            dlist = []
            elist = []
            flist = []
            if b == "s" or b == "S":
                
                for i in range (n):
                        course = raw_input("pls enter the name of the course %d\n"%(i+1))
                        elist += [course]
                        score= float(raw_input("pls enter the the score for  %s>>>\n"%(elist[i])))
                        alist +=[score]
                        unit = float(raw_input("pls enter the unit of the course%s>>>\n"%(i+1)))
                        blist +=[unit]
                        
                        asum = asum +unit
                      
                        if  score >= 70:
                                grade = "A"
                                y = 5
                                point = 5 *unit
                        
                        elif  score>=60:
                                grade = "B"
                                y = 4
                                point = 4* unit
                        elif  score >=50:
                                grade = "C"
                                y = 3
                                point = 3* unit
                        elif  score >= 45:
                                grade = "D"
                                y = 2
                                point = 2 * unit
                        elif  score >=40:
                                grade = "E"
                                y = 1
                                point = 1 * unit
                        else:
                                grade = "F"
                                y = 0
                                point = y* unit
                        clist +=[point]
                        dlist +=[grade]
                        tsum =tsum + point
                gp = tsum/asum
                print " "
                print"          This program calculate the grade point average of a student\n   "
                
                print"      The student  with name %s with matric no %s has a cgpa of %.2f\n This is result listed below\n    "%(name,matricno,gp)
                
                print"%12s%12s%12s%12s%12s\n"%("course","score","unit","point","grade")
                for i in range (n):
                        print"%12s%12d%12d%12d%12s"%(elist[i],alist[i],blist[i],clist[i],dlist[i])
            
                print "   "
                print"d program was written by linux call +2348166544879 for help"
            else:
                for i in range (n):
                    course = raw_input("pls enter the name of the course %d\n"%(i+1))
                    elist += [course]
                    grade= raw_input("pls enter the grade for %s\n"%(elist[i]))
                    flist += [grade]
                    unit = int(raw_input("enter the unit of the course for %s\n"%(elist[i])))
                    blist +=[unit]
                   
                    asum = asum +unit

                    if grade == "A" or grade == "a":
                        y=5
                        point = y * unit
                    if grade == "B" or grade == "b":
                        y=4
                        point = y * unit
                    if grade == "c" or grade == "C":
                        y=3
                        point = y * unit
                    if grade  == "d" or grade == "D":
                        y = 2
                        point = y * unit
                    if grade == "e" or grade == "E":
                        y = 1
                        point = y * unit
                    if grade == "f" or grade == "F":
                        y = 0
                        point = Y * unit
                    
                    clist +=[point]
                    dlist +=[grade]
                    tsum = tsum + point
                gp = tsum/asum
                print " "
                print"          This program calculate the grade point average of a student\n   "
                print"  The student  with name %s with matric no %s has a cgpa of %.2f \n This is result  listed below\n    "%(name,matricno,gp)

                print"%12s%12s%12s%12s\n"%("course","grade","unit","point")
                for i in range (n):
                                print"%12s%12s%12d%12d"%(elist[i],dlist[i],clist[i],blist[i])
                    
                print "   "
                print"d program was written by linux call +2348166544879 for help"
                        
            main()    

main()
