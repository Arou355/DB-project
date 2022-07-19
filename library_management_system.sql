CREATE TABLE `student` (
  `student_id` integer,
  `student_name` text,
  `student_gender` text
);

CREATE TABLE `book` (
  `book_id` integer,
  `book_title` text,
  `book_author` text,
  `book_publisher` text,
  `book_copies` integer,
  `book_cost` integer
);

CREATE TABLE `users` (
  `staff_id` integer,
  `staff_name` text,
  `staff_contact` text,
  `staff_mail` text,
  `staff_password` text,
  `staff_address` text
);

CREATE TABLE `relating` (
  `borrowers_id` integer,
  `book_id` integer,
  `student_id` integer,
  `staff_id` integer
);

ALTER TABLE `student` ADD FOREIGN KEY (`student_id`) REFERENCES `relating` (`student_id`);

ALTER TABLE `users` ADD FOREIGN KEY (`staff_id`) REFERENCES `relating` (`staff_id`);

ALTER TABLE `book` ADD FOREIGN KEY (`book_id`) REFERENCES `relating` (`book_id`);
