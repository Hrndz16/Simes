--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

-- Started on 2024-04-03 14:12:23

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'LATIN8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 18171)
-- Name: eventos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.eventos (
    idevento integer NOT NULL,
    fechaevento date NOT NULL,
    descrievento text NOT NULL
);


ALTER TABLE public.eventos OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 18170)
-- Name: eventos_idevento_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.eventos ALTER COLUMN idevento ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.eventos_idevento_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 215 (class 1259 OID 18162)
-- Name: usuarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuarios (
    idusuario integer NOT NULL,
    tipoid text NOT NULL,
    tipousuario integer NOT NULL,
    nomusuario text NOT NULL,
    apeusuario text,
    correousuario text NOT NULL,
    contrausuario text NOT NULL,
    fotousuario bytea
);


ALTER TABLE public.usuarios OWNER TO postgres;

--
-- TOC entry 4787 (class 0 OID 18171)
-- Dependencies: 217
-- Data for Name: eventos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.eventos (idevento, fechaevento, descrievento) FROM stdin;
1	2024-04-01	Exposicion corona de oro
\.


--
-- TOC entry 4785 (class 0 OID 18162)
-- Dependencies: 215
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuarios (idusuario, tipoid, tipousuario, nomusuario, apeusuario, correousuario, contrausuario, fotousuario) FROM stdin;
1087642625	CC	1	Marlon	Hernandez	marlonhergom70@gmail.com	marlon123	\N
1	TI	3	Sebastian	Armero	sebastian@gmail.com	1234	\N
12344	CC	3	Juanito	Perez	juanito@gmail.com	jaunito123	\N
\.


--
-- TOC entry 4793 (class 0 OID 0)
-- Dependencies: 216
-- Name: eventos_idevento_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.eventos_idevento_seq', 1, true);


--
-- TOC entry 4641 (class 2606 OID 18175)
-- Name: eventos eventos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.eventos
    ADD CONSTRAINT eventos_pkey PRIMARY KEY (idevento);


--
-- TOC entry 4639 (class 2606 OID 18168)
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (idusuario);


-- Completed on 2024-04-03 14:12:25

--
-- PostgreSQL database dump complete
--

