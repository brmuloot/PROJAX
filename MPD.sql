CREATE TABLE IF NOT EXISTS utilisateur(
    id_user INT PRIMARY KEY,
    role varchar(50),
    pseudo varchar(50),
    mot_de_passe TEXT,
    email varchar(50)
);

CREATE TABLE IF NOT EXISTS post(
    id_post INT PRIMARY KEY,
    post TEXT,
    user varchar(50),
    date datetime,
    titre varchar(255)
);

CREATE TABLE IF NOT EXISTS like(
    id_post_like INT,
    id_user_like INT,
    FOREIGN KEY (id_post_like) REFERENCES post(id_post),
    FOREIGN KEY (id_user_like) REFERENCES utilisateur(id_user)
);

CREATE TABLE IF NOT EXISTS commentaire(
    id_commentaire INT PRIMARY KEY,
    commentaire TEXT,
    id_post INT,
    id_user INT,
    date datetime,
    FOREIGN KEY (id_post) REFERENCES post(id_post),
    FOREIGN KEY (id_user) REFERENCES utilisateur(id_user)
);

-- INSERTION DE DONNEE DE TEST

INSERT INTO utilisateur (id_user, role, pseudo, mot_de_passe, email)
VALUES
(1, "Admin", "Rémax", "RémaxLeBadax", "remilamax@max.com"),
(2, "Visiteur", "None", "None", "None"),
(3, "Utilisateur", "Lakhbix", "mo dou pass","Singhax_la_menax@climax.com");

INSERT INTO post (id_post, post, user, date, titre)
VALUES
    (1, 'Contenu du premier post', 'Rémax', '2023-11-15 10:00:00', 'Premier Post'),
    (2, 'Contenu du deuxième post', 'Rémax', '2023-11-16 12:30:00', 'Deuxième Post'),
    (3, 'Contenu du troisième post', 'Rémax', '2023-11-17 09:45:00', 'Troisième Post');

INSERT INTO commentaire (id_commentaire, commentaire, id_post, id_user)
VALUES
(1, "la max ce overbax de malax", 2, 1),
(2, "This is amazing guy I love this man, MY BOY REMAAAAAAAAAAAX", 1, 3);

INSERT INTO "like" (id_post_like, id_user_like)
VALUES
("1", "2"),
("1","1"),
("2","3");

-- COMPTER LE NOMBRE DE LIKE SUR UNE PUBLICATION ET POUR UNE PERSONNE 

SELECT id_post_like, COUNT(*) AS nombre_likes_post
FROM like
GROUP BY id_post_like;

SELECT id_user_like, COUNT(*) AS nombre_liks_user
FROM like
GROUP BY id_user_like;