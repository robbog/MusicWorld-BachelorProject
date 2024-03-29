USE [master]
GO
/****** Object:  Database [MusicWorld]    Script Date: 29.04.2021 21:05:15 ******/
CREATE DATABASE [MusicWorld]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'MusicWorld2', FILENAME = N'D:\Programy E\SQL Server nowy\MSSQL15.MSSQLSERVER\MSSQL\DATA\MusicWorld2.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'MusicWorld2_log', FILENAME = N'D:\Programy E\SQL Server nowy\MSSQL15.MSSQLSERVER\MSSQL\DATA\MusicWorld2_log.ldf' , SIZE = 73728KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [MusicWorld] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [MusicWorld].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [MusicWorld] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [MusicWorld] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [MusicWorld] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [MusicWorld] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [MusicWorld] SET ARITHABORT OFF 
GO
ALTER DATABASE [MusicWorld] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [MusicWorld] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [MusicWorld] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [MusicWorld] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [MusicWorld] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [MusicWorld] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [MusicWorld] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [MusicWorld] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [MusicWorld] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [MusicWorld] SET  DISABLE_BROKER 
GO
ALTER DATABASE [MusicWorld] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [MusicWorld] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [MusicWorld] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [MusicWorld] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [MusicWorld] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [MusicWorld] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [MusicWorld] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [MusicWorld] SET RECOVERY FULL 
GO
ALTER DATABASE [MusicWorld] SET  MULTI_USER 
GO
ALTER DATABASE [MusicWorld] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [MusicWorld] SET DB_CHAINING OFF 
GO
ALTER DATABASE [MusicWorld] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [MusicWorld] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [MusicWorld] SET DELAYED_DURABILITY = DISABLED 
GO
EXEC sys.sp_db_vardecimal_storage_format N'MusicWorld', N'ON'
GO
ALTER DATABASE [MusicWorld] SET QUERY_STORE = OFF
GO
USE [MusicWorld]
GO
/****** Object:  Table [dbo].[Top_artists_longterm]    Script Date: 29.04.2021 21:05:17 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Top_artists_longterm](
	[Position] [int] NULL,
	[Artist_spotifyID] [nvarchar](255) NULL,
	[Artist_uri] [nvarchar](255) NULL,
	[Artist] [nvarchar](255) NULL,
	[Genre] [nvarchar](255) NULL,
	[Img_url] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Top_artists_shortterm]    Script Date: 29.04.2021 21:05:17 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Top_artists_shortterm](
	[Position] [int] NULL,
	[Artist_spotifyID] [nvarchar](255) NULL,
	[Artist_uri] [nvarchar](255) NULL,
	[Artist] [nvarchar](255) NULL,
	[Genre] [nvarchar](255) NULL,
	[Img_url] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Top_tracks_longterm]    Script Date: 29.04.2021 21:05:17 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Top_tracks_longterm](
	[Position] [int] NULL,
	[Track_spotifyID] [nvarchar](255) NULL,
	[Track_uri] [nvarchar](255) NULL,
	[Title] [nvarchar](255) NULL,
	[Artist] [nvarchar](255) NULL,
	[Album] [nvarchar](255) NULL,
	[Img_url] [nvarchar](255) NULL,
	[Track_popularity] [nvarchar](8) NULL,
	[Track_danceability] [numeric](8, 4) NULL,
	[Track_energy] [numeric](8, 4) NULL,
	[Track_valence] [numeric](8, 4) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Top_tracks_shortterm]    Script Date: 29.04.2021 21:05:17 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Top_tracks_shortterm](
	[Position] [int] NULL,
	[Track_spotifyID] [nvarchar](255) NULL,
	[Track_uri] [nvarchar](255) NULL,
	[Title] [nvarchar](255) NULL,
	[Artist] [nvarchar](255) NULL,
	[Album] [nvarchar](255) NULL,
	[Img_url] [nvarchar](255) NULL,
	[Track_popularity] [nvarchar](8) NULL,
	[Track_danceability] [numeric](8, 4) NULL,
	[Track_energy] [numeric](8, 4) NULL,
	[Track_valence] [numeric](8, 4) NULL
) ON [PRIMARY]
GO
USE [master]
GO
ALTER DATABASE [MusicWorld] SET  READ_WRITE 
GO
