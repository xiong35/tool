tableHTML = """
    <table class="paste">
      <tbody>
        <tr>
          <td class="linenum">
            <div>
              <pre>{}</pre>
            </div>
          </td>
          <td class="code">
            <div>
              <pre>{}</pre>
            </div>
          </td>
        </tr>
      </tbody>
    </table>"""

with open('./src/htmlTemplate/template.html', 'r') as fr:
    lines = fr.readlines()

fullHTML = ''

for line in lines:
    fullHTML += line
