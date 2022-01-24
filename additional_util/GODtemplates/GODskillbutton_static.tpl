Group
{
	name = "All Groups"
	type = "list"

	Variable
	{
		name = "Include File"
		class = "static"
		type = "include"
		description = ""
		value = ""
		defaultValue = "database\Templates\InGameUI\Includes\StringRollover.tpl"
	}

	Group
	{
		name = "Header"
		type = "system"

		Variable
		{
			name = "ActorName"
			class = "variable"
			type = "string"
			description = ""
			value = ""
			defaultValue = ""
		}

		Variable
		{
			name = "Class"
			class = "static"
			type = "string"
			description = ""
			value = ""
			defaultValue = ""
		}

		Variable
		{
			name = "FileDescription"
			class = "variable"
			type = "string"
			description = ""
			value = ""
			defaultValue = "ButtonStatic"
		}

	}

	Group
	{
		name = "Config"
		type = "list"

		Variable
		{
			name = "bitmapNameUp"
			class = "picklist"
			type = "string"
			description = ""
			value = ""
			defaultValue = "InGameUI\SkillButtonBorderRound01.tex;InGameUI\SkillButtonBorder01.tex"
		}

		Variable
		{
			name = "bitmapNameDown"
			class = "picklist"
			type = "string"
			description = ""
			value = ""
			defaultValue = "InGameUI\SkillButtonBorderRoundDown01.tex;InGameUI\SkillButtonBorderDown01.tex"
		}

		Variable
		{
			name = "bitmapNameInFocus"
			class = "picklist"
			type = "string"
			description = ""
			value = ""
			defaultValue = "InGameUI\SkillButtonBorderRoundOver01.tex;InGameUI\SkillButtonBorderRoundOver01.tex"
		}

		Variable
		{
			name = "bitmapNameDisabled"
			class = "variable"
			type = "file_tex"
			description = ""
			value = ""
			defaultValue = ""
		}

		Variable
		{
			name = "soundNameUp"
			class = "variable"
			type = "file_dbr"
			description = ""
			value = ""
			defaultValue = ""
		}

		Variable
		{
			name = "soundNameDown"
			class = "variable"
			type = "file_dbr"
			description = ""
			value = ""
			defaultValue = "Records\Sounds\SoundPak\UI\AddSkillPointPak.dbr"
		}

		Variable
		{
			name = "isCircular"
			class = "variable"
			type = "bool"
			description = ""
			value = ""
			defaultValue = ""
		}

		Variable
		{
			name = "bitmapPositionX"
			class = "variable"
			type = "int"
			description = "Upper Left Corner"
			value = ""
			defaultValue = ""
		}

		Variable
		{
			name = "bitmapPositionY"
			class = "variable"
			type = "int"
			description = "Upper Left Corner"
			value = ""
			defaultValue = ""
		}

	}

}

