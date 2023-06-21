class HtmlTable:

    def __init__(self, data):
        self.data = data

    def get_table(self):
        table = ["<table>"]
        table.append("<tr><th>Name</th><th>Symbol</th><th>Price</th><th>Last Update</th></th>")
        for item in self.data:
            table.append("<tr>")
            for row in item[1:]:
                table.append(f"<td>{row}</td>")
            table.append("</tr>")
        table.append("</table>")
        return "".join(table)
