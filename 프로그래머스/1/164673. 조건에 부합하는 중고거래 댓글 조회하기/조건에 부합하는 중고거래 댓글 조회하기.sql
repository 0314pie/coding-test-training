-- 코드를 입력하세요
SELECT b.title "게시글 제목", b.board_id "게시글 ID", r.reply_id "댓글 ID", r.writer_id "댓글 작성자 ID", r.contents "댓글 내용", to_char(r.created_date, 'YYYY-MM-DD') "댓글 작성일"
from used_goods_board b, used_goods_reply r
where b.board_id = r.board_id
and to_char(b.created_date, 'YYYY-MM') = '2022-10'
order by r.created_date, b.title;