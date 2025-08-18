def solution(genres, plays):
    
    genre_dict = {}
    for i in range(len(genres)):
        genre = genres[i]
        play_count = plays[i]
        try:
            genre_dict[genre][0] += play_count
            genre_dict[genre][1].append((i, play_count))
        except KeyError:
            genre_dict[genre] = [play_count, [(i, play_count)]]

    for genre in genre_dict.keys():
        genre_dict[genre][1] = sorted(genre_dict[genre][1], key=lambda x:x[1],reverse=True)
    
    sorted_genre_by_plays = sorted(list(genre_dict.items()),key=lambda x: x[1][0], reverse=True)
    answer = []
    for genre_play in sorted_genre_by_plays:
        for i in range(2):
            try:
                answer.append(genre_play[1][1][i][0])
            except IndexError:
                continue
            
    return answer
