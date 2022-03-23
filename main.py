question_list = [
    'What comes after 2? \na>1 \nb>3\nc>4\nd>5\n',
    'What color is a Banana? \na>Red \nb>Brown\nc>Blue\nd>Yellow\n',
    'What sound does a Lion makes?\na>Roar \nb>Bark\nc>Meow\nd>English\n',
    'What color is a Panda?\na>Red and Blue \nb>Brown and Pink\nc>Black and White \nd>Violet and Purple\n',
    'Can a bird fly? \na>Yes \nb>No\n',
]


class mcq:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.ans = answer


correct_ans = [
    mcq(question_list[0], 'b'),
    mcq(question_list[1], 'd'),
    mcq(question_list[2], 'a'),
    mcq(question_list[3], 'c'),
    mcq(question_list[4], 'a'),
]


def run_test(correct_ans):
    score = 0
    for question in correct_ans:
        ans = input(question.prompt)
        if ans == question.ans:
            score += 1
    print('You scored', score, '/', len(question_list),
          ' in the test. \nGood Luck')

    
    import random
    bq = random.randint(1, 5)
    if bq == 3:
        print('Looks like its your lucky day \nHere comes a bonus question:- ')
        print('Who won the race in the famous tortoise and hare story? \na>Hare \nb>Tortoise\n')
        ans2 = input()
        if ans2 == 'b':
            score += 1
            print(f'Thats great! \nYour final score is {score}/{len(question_list)}. Enjoy your day!')
    else:
        print("Sorry,No bonus question this time:(")


run_test(correct_ans)