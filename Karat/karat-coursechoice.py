def matchcourse(pairs, student1, student2):
    studentToCourse = {}
    courseToStudent = {}
    for student, course in pairs:
        student = int(student)
        if student not in studentToCourse:
            studentToCourse[student] = set()
        if course not in courseToStudent:
            courseToStudent[course] = set()
        courseToStudent[course].add(student)
        studentToCourse[student].add(course)
    res = []
    if student1 not in studentToCourse:
        return res
    for course in studentToCourse[student1]:
        if student2 in courseToStudent[course]:
            res.append(course)
    return res
student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]
def buildGraph(pairs, start, destination):
    shouldBefore = {}
    shouldAfter = {}
    courses = set()
    for before, after in pairs:
        if after not in shouldBefore:
            shouldBefore[after] = set()
        if before not in shouldAfter:
            shouldAfter[before] = set()
        shouldBefore[after].add(before)
        shouldAfter[before].add(after)
        courses.add(before)
        courses.add(after)
    visited = set()
    def dfs(v, dependency):
        if v in visited:
            return
        visited.add(v)
        if v in dependency:
            for n in dependency[v]:
                dfs(n, dependency)
    dfs(start, shouldBefore)
    dfs(destination, shouldAfter)
    res = []
    for c in courses:
        if c not in visited:
            res.append(c)
    print(courses)
    print(visited)
    return res
allCourses = [
  ['Logic', 'COBOL'],
  ['Data Structures', 'Algorithms'],
  ['Creative Writing', 'Data Structures'],
  ['Algorithms', 'COBOL'],
  ['Intro to Computer Science', 'Data Structures'],
  ['Logic', 'Compilers'],
  ['Data Structures', 'Logic'],
  ['Creative Writing', 'System Administration'],
  ['Databases', 'System Administration'],
  ['Creative Writing', 'Databases'],
  ['Intro to Computer Science', 'Graphics'],
];
print(buildGraph(allCourses, "Data Structures", "Databases"))
def middleCourse(pairs, start, end):
    shouldBefore = {}
    shouldAfter = {}
    courses = set()
    for pair in  pairs:
        before, after = pair
        if before not in shouldAfter:
            shouldAfter[before] = []
        shouldAfter[before].append(after)
        if after not in shouldBefore:
            shouldBefore[after] = []
        shouldBefore[after].append(before)
        courses.add(after)
        courses.add(before)
    visited = set()
    def dfs(node, dictionry):
        if node in visited:
            return
        visited.add(node)
        if node in dictionry:
            for n in dictionry[node]:
                dfs(n, dictionry)
    dfs(start, shouldBefore)
    dfs(end, shouldAfter)
    res = []
    for c in courses:
        if c not in visited:
            res.append(c)
    return res
    


