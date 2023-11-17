CREATE TABLE utilisateur(
    id_user INT PRIMARY KEY,
    role varchar(50),
    pseudo varchar(50),
    mot_de_passe TEXT,
    email varchar(50)
);

CREATE TABLE post(
    id_post INT PRIMARY KEY,
    post TEXT,
    user varchar(50),
    date datetime,
    titre, varchar(255)
);

CREATE TABLE like(
    id_post_like INT,
    id_user_like INT,
    FOREIGN KEY (id_post_like) REFERENCES post(id_post),
    FOREIGN KEY (id_user_like) REFERENCES user(id_user)
);

CREATE TABLE commentaire(
    id_commentaire INT PRIMARY KEY,
    commentaire TEXT,
    id_post INT,
    id_user INT,
    date datetime,
    FOREIGN KEY (id_post) REFERENCES post(id_post),
    FOREIGN KEY (id_user) REFERENCES post(id_user)
);