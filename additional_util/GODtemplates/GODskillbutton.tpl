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
		defaultValue = "custommaps\goodolddays\additional_util\GODtemplates\GODskillbutton_static.tpl"
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
			defaultValue = ""
		}

	}

	Group
	{
		name = "Config"
		type = "list"

		Variable
		{
			name = "skillName"
			class = "variable"
			type = "file_dbr"
			description = ""
			value = ""
			defaultValue = ""
		}

		Variable
		{
			name = "skillOffsetX"
			class = "variable"
			type = "int"
			description = ""
			value = ""
			defaultValue = "4"
		}

		Variable
		{
			name = "skillOffsetY"
			class = "variable"
			type = "int"
			description = ""
			value = ""
			defaultValue = "4"
		}

	}

}

fileNameHistoryEntry
{
	"Templates\InGameUI\New Template.tpl"
}
