def convert_to_numeric(score):
    """    Conc=vert a score to numerical type  """
    converted_score = float(score)
    return converted_score


def sum_of_middle_three(score1, score2, score3, score4, score5):
    min_score = min(score1, score2, score3, score4, score5)
    max_score = max(score1, score2, score3, score4, score5)
    sum_of_middle_three = score1 + score2 + score3 + score4 + score5 - min_score - max_score
    return sum_of_middle_three


def score_to_rating_string(average_score):
    if 0 <= average_score < 1:
        rating = "Terrible"
    elif 1 <= average_score < 2:
        rating = "Bad"
    elif 2 <= average_score < 3:
        rating = "OK"
    elif 3 <= average_score < 4:
        rating = "Good"
    else:
        rating = "Excellent"
    return rating


def scores_to_rating(score1, score2, score3, score4, score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    # STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    # STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1, score2, score3, score4, score5) / 3

    # STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating


rating = scores_to_rating(1, "2", 3.3, 4.5, 2)
print(rating)
